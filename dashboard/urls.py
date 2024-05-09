from django.urls import path
from .views import List_products , Add_products , Add_category , Update_product, Delete_product 

urlpatterns = [
    path('products/', List_products.as_view(), name='list_products'),
    path('products/add/', Add_products.as_view(), name='add_product'),
    path('products/edit/<int:pk>/', Update_product.as_view(), name='edit_product'),
    path('products/delete/<int:pk>/', Delete_product.as_view(), name='delete_product'),
    path('categories/add', Add_category.as_view(), name='add_category')
]
    
