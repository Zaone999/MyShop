# urls.py in your Django project or application
from django.urls import path
from django.contrib.auth import views as auth_views
from users.views import Create_Profile
#from .views import Create_Profile, View_Profile

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logged_out.html'), name='logout'), 
    path('signup/', Create_Profile.as_view(), name='signup'), # Ensure this line is correct
#    path('view_profile/<int:pk>', View_Profile.as_view(), name='view_profile')
]