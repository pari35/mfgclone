
from django import views
from django.contrib import admin
from django.urls import path
# from .views import home
from . import views
urlpatterns = [
    path('home/', views.home,name="home"),
    path('amenities/',views.amenities,name='amenities'),
    path('configuration/',views.configurations,name='configuration'),
    path('connector/',views.connector,name='connector'),
    path('connector/delete-data/',views.delete_data,name="delete-data"),
    path('registration/',views.register,name="admin-register"),
    path('',views.login,name="login"),

    
    ]