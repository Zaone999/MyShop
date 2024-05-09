from django.test import TestCase
from shop.models import Product, Category
from django.urls import reverse



class ProductTests(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name="Shoe" , description="Shoe category")        
        Product.objects.create(category = self.category, name="Test Shoe", description="Test Description", price=100.00, stock_quantity=10, size="10", color="Red")
        self.data = {
        'name': 'New Shoe',
        'description': 'Comfortable casual shoes',
        'price': 120.50,
        'stock_quantity': 15,
        'size': '9',
        'color': 'Blue',
        'category':self.category.id  # Ensure the category ID is included in the form data
    }

    def test_product_list_view(self):
        response = self.client.get(reverse('list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name="Test Shoe").exists())
        self.assertContains(response, "Test Shoe")
        
    
    def test_add_product_view(self):
        response = self.client.post(reverse('add_product'), self.data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Product.objects.filter(name="New Shoe").exists())
               