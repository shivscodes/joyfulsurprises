from django.urls import path
from .views import register, user_login, home, product

urlpatterns = [
    path('register/', register, name='register'),
    path("home/", home, name="home"),
    path("product/", product, name="product"),
    path('', user_login, name='login'),
    # Add your other app URLs here
]
