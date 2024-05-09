from django.db import models
from shop.models import Product

# Create your models here.
class Inventory(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    quantity_added = models.IntegerField(default=0)