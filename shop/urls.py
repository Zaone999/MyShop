from .views import List_Products
from django.urls import path

urlpatterns = [
    path('', List_Products.as_view(), name='home')
]