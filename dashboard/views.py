from django.shortcuts import render
from django.http import HttpResponse
from shop.models import Product

def list_products(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product_list.html', {'products': products})