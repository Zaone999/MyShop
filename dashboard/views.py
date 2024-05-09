from django.shortcuts import render, redirect 
from shop.models import Product
from .forms import ProductForm

def list_products(request):
    products = Product.objects.all()
    return render(request, 'dashboard/product_list.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'dashboard/create_product.html', {'form' : form})