from django.urls import path
from .views import Add_products , Add_category , Update_product, Delete_product, dashboard_view, export_products_csv, export_products_xlsx
urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('products/add/', Add_products.as_view(), name='add_product'),
    path('products/edit/<int:pk>/', Update_product.as_view(), name='edit_product'),
    path('products/delete/<int:pk>/', Delete_product.as_view(), name='delete_product'),
    path('categories/add', Add_category.as_view(), name='add_category'),
    path('dashboard/export/csv', export_products_csv, name='export_csv'),
    path('dashboard/export/xlsx', export_products_xlsx, name='export_xlsx')
]
    
