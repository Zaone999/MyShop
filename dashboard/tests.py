from django.test import TestCase
from shop.models import Product, Category
from django.urls import reverse

class CategoryTests(TestCase):
    
    def test_add_category(self):
        self.category = Category.objects.create(name="new category" , description="a category")
        self.assertTrue(Category.objects.filter(name="new category").exists())
        response = self.client.post(reverse('add_category'), {
            'name' : 'other new category',
            'description' : self.category.description
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Category.objects.filter(name="other new category").exists())
        
class ProductTests(TestCase):
    
    def setUp(self):
        self.category = Category.objects.create(name="Shoe" , description="Shoe category")        
        self.product = Product.objects.create(category = self.category, name="Test Shoe", description="Test Description", price=100.00, stock_quantity=10, size="10", color="Red")
        self.other_product = Product.objects.create(category = self.category, name="Another Test Shoe", description="Test Description", price=100.00, stock_quantity=10, size="10", color="Red")

        self.data = {
            'name': 'New Shoe',
            'description': 'Comfortable casual shoes',
            'price': 120.50,
            'stock_quantity': 15,
            'size': '9',
            'color': 'Blue',
            'category':self.category.id
        }
        self.editedData = {
            'name': 'New Shoe',
            'description': 'Very Comfortable casual shoes',
            'price': 18.50,
            'stock_quantity': 20,
            'size': '9',
            'color': 'Blue',
            'category':self.category.id
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
        
    def test_edit_product_view(self):
        self.client.post(reverse('edit_product' , args=[self.product.id]), self.editedData)
        self.assertTrue(Product.objects.filter(pk=self.product.id, description="Very Comfortable casual shoes", price=18.50, stock_quantity=20).exists())
        self.assertEqual(len(list(Product.objects.all())), 2)
        
    def test_delete_product_view(self):
        self.client.post(reverse('delete_product' , args=[self.product.id]))
        self.assertEqual(len(list(Product.objects.all())), 1)