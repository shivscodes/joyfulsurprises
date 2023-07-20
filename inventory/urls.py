from .views import *
from django.urls import path
from django.urls import re_path
from inventory import views


urlpatterns = [
    path('create-inventory/', views.create_inventory, name='create_inventory'),
]