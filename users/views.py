from django.forms import BaseModelForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .forms import NormalUserCreationForm
from .models import Profile

class Create_Profile(CreateView):
    model = Profile
    form_class = NormalUserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("login")