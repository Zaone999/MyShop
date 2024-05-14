from django.db import models
from django.contrib.auth.models import AbstractUser

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