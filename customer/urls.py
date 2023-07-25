from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, HomeView
from .views import  product, product_display

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path("", HomeView.as_view(), name="home"),
    path("product/", product, name="product"),
    path("buy/", product_display, name="product_display"),
    # Add your other app URLs here
]
