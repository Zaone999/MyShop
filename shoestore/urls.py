from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('owner/', include('dashboard.urls')),    
    path('profiles/', include('users.urls')), 
    path('home/', include('shop.urls')),
    path('', include('shop.urls'))
    ]
