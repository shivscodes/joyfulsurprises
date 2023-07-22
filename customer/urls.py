from django.urls import path
from .views import register, user_login, user_logout, home, product, product_display

urlpatterns = [
    path('register/', register, name='register'),
    path("", home, name="home"),
    path("product/", product, name="product"),
    path("buy/", product_display, name="product_display"),
    path('login', user_login, name='login'),
    path('user_logout', user_logout, name='user_logout'),
    # Add your other app URLs here
]
