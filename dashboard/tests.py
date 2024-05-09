from django.test import TestCase
from shop.models import Product, Category
from django.urls import reverse



class ProductTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name="Shoe" , description="Shoe category")        
        Product.objects.create(category=cls.category, name="Test Shoe", description="Test Description", price=100.00, stock_quantity=10, size="10", color="Red")


    def test_product_list_view(self):
        response = self.client.get(reverse('list_products'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Shoe")        