from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from .models import Profile

# Create your views here.
class Create_Profile(CreateView):
    model = Profile
    form_class = CustomUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")