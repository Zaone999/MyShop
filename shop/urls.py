from .views import List_products
from django.urls import path
from users.views import add_to_cart, delete_from_cart
urlpatterns = [
    path('', List_products.as_view(), name='home'),
    path('cart/add/<int:product_id>', add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:cart_item_id>', delete_from_cart, name='delete_from_cart')
]