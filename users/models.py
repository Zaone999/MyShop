from django.db import models
from django.contrib.auth.models import AbstractUser
from shop.models import Product 
# Create your models here.
class Profile(AbstractUser):
     # Define roles available
    USER = 'user'
    STAFF = 'staff'
    OWNER = 'owner'
    ROLE_CHOICES = [
        (USER, 'User'),   # Ordinary site user
        (STAFF, 'Staff'), # Site administrators or staff who manage content
        (OWNER, 'Owner'), # Owners who manage high-level aspects of the site
    ]

    # Additional field to define user role
    role = models.CharField(
        max_length=7,
        choices=ROLE_CHOICES,
        default=USER,
    )  
      
class Cart(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Cart of {self.user.username}'
    
    def contains(self):
        return self.items.all()
    
    def total_price(self):
        return sum(item.product.price * item.quantity for item in self.items.all())

    def item_count(self):
        return self.items.count()
               
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'