from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import NormalUserCreationForm
from .models import Profile, Cart, CartItem
from shop.models import Product
from django.contrib.auth import views as auth_views

class Create_Profile(CreateView):
    model = Profile
    form_class = NormalUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")

class ALoginView(auth_views.LoginView):
    template_name = 'users/login.html'
    
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cartItem.quantity += 1
    cartItem.save()
    return redirect('home')

def delete_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
    return redirect('home')