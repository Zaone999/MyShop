from django.urls import path
from .views import list_products #, add_product, update_product, delete_product 

urlpatterns = [
    path('products/', list_products, name='list_products'),
#        path('products/add/', add_product, name='add_product'),
#        path('product/edit/<int:pk>/', update_product, name='update_product'),
#        path('product/delete/<int:pk>/', delete_product, name='delete_product'),

]
    
