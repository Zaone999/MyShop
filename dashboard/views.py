from shop.models import Product, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class List_products(ListView):
    model = Product
    template_name = 'dashboard/list_products.html'

class Add_products(CreateView):
    model = Product
    template_name = 'dashboard/add_product.html'
    fields = ['category','name', 'description', 'price', 'stock_quantity', 'size', 'color']
    success_url = reverse_lazy('list_products')
    
class Update_product(UpdateView):
    model = Product
    template_name = 'dashboard/update_product.html'
    fields = ['category','name', 'description', 'price', 'stock_quantity', 'size', 'color']
    success_url = reverse_lazy('list_products')

class Delete_product(DeleteView):
    model = Product
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('list_products') 

class Add_category(CreateView):
    model = Category
    template_name = 'dashboard/add_category.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('list_products')