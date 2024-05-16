from django.views.generic import ListView
from .models import Product

class List_Products(ListView):
    model = Product
    template_name = 'shop/list_products.html'