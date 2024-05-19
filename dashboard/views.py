from shop.models import Product, Category
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from users.models import Cart
from django.shortcuts import render
import csv
import openpyxl
from django.http import HttpResponse

class List_products(ListView):
    model = Product
    template_name = 'dashboard/list_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if (self.request.user.is_authenticated):
            context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
            print(context['cart'])
        return context
    
class Add_products(CreateView):
    model = Product
    template_name = 'dashboard/add_product.html'
    fields = ['category','name', 'description','quantity_added','image']
    success_url = reverse_lazy('list_products')
    
class Update_product(UpdateView):
    model = Product
    template_name = 'dashboard/update_product.html'
    fields = ['category','name', 'description','quantity_added','image']
    success_url = reverse_lazy('dashboard')

class Delete_product(DeleteView):
    model = Product
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard') 

class Add_category(CreateView):
    model = Category
    template_name = 'dashboard/add_category.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('dashboard')

def dashboard_view(request):
    query = request.GET.get('search')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'dashboard/dashboard.html', {'products': products})


def export_products_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="products.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Description', 'Price', 'quantity_added'])

    products = Product.objects.all()
    for product in products:
        writer.writerow([product.name, product.description, product.price, product.quantity_added])

    return response


def export_products_xlsx(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="products.xlsx"'

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Products"

    # Write header
    headers = ['Name', 'Description', 'Price', 'quantity_added']
    ws.append(headers)

    # Write data
    products = Product.objects.all()
    for product in products:
        ws.append([product.name, product.description, product.price, product.quantity_added])

    wb.save(response)
    return response
