from django.urls import path
from .views import List_products , Add_products , Add_category#, update_product, delete_product 

urlpatterns = [
    path('products/', List_products.as_view(), name='list_products'),
    path('products/add/', Add_products.as_view(), name='add_product'),
    path('categories/add', Add_category.as_view(), name='add_category')
#        path('product/edit/<int:pk>/', update_product, name='update_product'),
#        path('product/delete/<int:pk>/', delete_product, name='delete_product'),
]
    
