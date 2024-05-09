from django.shortcuts import render, redirect 
from shop.models import Product
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView

class List_products(ListView):
    model = Product
    template_name = 'dashboard/product_list.html'


class Add_products(CreateView):
    model = Product
    template_name = 'dashboard/create_product'
    fields = ['category','name', 'description', 'price', 'stock_quantity', 'size', 'color']
    success_url = reverse_lazy('list_products')