# urls.py in your Django project or application
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import ALoginView
from users.views import Create_Profile

urlpatterns = [
    path('login/', ALoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logged_out.html'), name='logout'), 
    path('signup/', Create_Profile.as_view(), name='signup'),
] 
