from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import NormalUserCreationForm
from .models import Profile, Cart, CartItem
from shop.models import Product
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

class Create_Profile(CreateView):
    model = Profile
    form_class = NormalUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")

class Update_Profile(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = "users.can_change_profile"
    model = Profile
    fields = ['username']
    success_url = reverse_lazy('home')
    template_name = "users/edit_profile.html"
    def get_object(self):
        return self.request.user

class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    permission_required = "users.can_change_profile"
    template_name = 'users/edit_password.html'
    success_url = reverse_lazy('home')
    form_class = PasswordChangeForm
    
    def get_success_url(self):
        return reverse_lazy('home')

@login_required   
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cartItem, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cartItem.quantity += 1
    cartItem.save()
    return redirect('home')

@login_required
def delete_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart__user=request.user)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
    return redirect('home')