from .helpers import get_super_categories, get_circle_categories, get_active_banners, get_subbanner, get_mobile_banners, get_left_containers, get_left_sub_images, get_right_containers,get_right_sub_images, get_product_detail_data
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm
from django.contrib.auth import logout, authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from inventory.models import *


class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'customer/customer_register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
        return render(request, 'customer/customer_register.html', {'form': form})


class UserLoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, 'customer/customer_login.html')

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Replace 'home' with the name of your home page URL pattern
            return redirect('home')
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        # Replace 'home' with the name of your home page URL pattern
        return redirect('home')


class HomeView(View):
    def get(self, request, **kwargs):
        drop_down_data = get_super_categories()
        #print(drop_down_data)
        circle_data = get_circle_categories()
        banner_data = get_active_banners()
        subbanner = get_subbanner()
        mobilebanner = get_mobile_banners()
        left_container = get_left_containers()
        left_sub_imgs = get_left_sub_images()
        right_container = get_right_containers()
        right_sub_imgs = get_right_sub_images()
        
        context = {
            "drop_down_data": drop_down_data,
            "circle_data": circle_data,
            "banner_data": banner_data,
            "subbanner": subbanner,
            "mobilebanner": mobilebanner,
            "left_container": left_container,
            "left_sub_imgs": left_sub_imgs,
            "right_container": right_container,
            "right_sub_imgs": right_sub_imgs,
        }

        return render(request, 'customer/customer_landing.html', context)


class ProductView(View):
    
    def get(self, request, **kwargs):
        product_data = get_product_detail_data()
        #print(product_data)
        drop_down_data = get_super_categories()
        context = {
            "product_data": product_data,
            "drop_down_data": drop_down_data
        }
        return render(request, 'customer/product.html', context)


def product_display(request, **kwargs):
    drop_down_data = get_super_categories()
    context = {
            "drop_down_data": drop_down_data
        }
    return render(request, 'customer/customer_home.html', context)
