from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/', default='default.webp')
    price = models.PositiveIntegerField(default=50)
    last_updated = models.DateTimeField(auto_now=True)
    quantity_added = models.PositiveBigIntegerField(default=0)
    def __str__(self):
        return self.name