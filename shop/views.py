from django.views.generic import ListView
from .models import Product, Category
from users.models import Cart

class List_products(ListView):
    model = Product
    template_name = 'dashboard/list_products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        if (self.request.user.is_authenticated):
            context['cart'], created = Cart.objects.get_or_create(user=self.request.user)
        if (self.request.user.has_perm('users.access_dashboard')):
            context['owner'] = True
        return context