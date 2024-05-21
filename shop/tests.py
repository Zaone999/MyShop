from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from shop.models import Product
from shop.models import Category
from users.models import Cart, CartItem

# Create your tests here.
class TestCartFunctions(TestCase):
    def setUp(self):
        self.User = get_user_model()

        self.login_url = reverse('login')
    
        self.valid_login_data = {
            'username': 'testuser',
            'password': 'testpassword123'
        }
        self.category = Category.objects.create(name="Shoe" , description="Shoe category")        
        self.product = Product.objects.create(category = self.category, name="Test Shoe", description="Test Description", price=100.00)
        self.product2 = Product.objects.create(category = self.category, name="Second Test Shoe", description="Test Description", price=100.00)

    def test_add_to_cart(self):
        self.User.objects.create_user(username='testuser', password='testpassword123')
        # login in
        response = self.client.post(self.login_url, self.valid_login_data)
        user = response.wsgi_request.user
        # add items to cart
        self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.client.get(reverse('add_to_cart', args=[self.product.id]))
        self.client.get(reverse('add_to_cart', args=[self.product2.id]))
        
        cart = Cart.objects.get(user=user)
        print(cart.contains())
        self.assertEqual(len(cart.items.all()), 2)