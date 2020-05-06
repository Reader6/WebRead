from django.urls import path
from login import views
from django.contrib import admin
app_name='login';
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('logins_search/',views.logins_search),
    path('yonghu/', views.user),
]