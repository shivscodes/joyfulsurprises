from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, HomeView, ProductView
from .views import  product_display
from django.urls import re_path

urlpatterns = [
    re_path(r'^register/?$', RegisterView.as_view(), name='register'),
    re_path(r'^login/?$', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='user_logout'),
    path("", HomeView.as_view(), name="home"),
    re_path(r'^product/?$', ProductView.as_view(), name="product"),
    re_path(r'^buy/?$', product_display, name="product_display"),
    # Add your other app URLs here
]
