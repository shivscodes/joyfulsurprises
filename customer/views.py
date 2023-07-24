from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout

from inventory.models import *

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'customer/customer_register.html', {'form': form})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home page URL pattern
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'customer/customer_login.html')
    
def user_logout(request):
    logout(request)
    return redirect('home')

from rest_framework.response import Response
from rest_framework.decorators import api_view
from inventory.models import SuperCategory
from inventory.serializers import SuperCategorySerializer
from django.db.models import Prefetch
import json

@api_view(['GET'])
def home(request, **kwargs):
    # Fetch all the SuperCategory objects along with related Categories and Subcategories
    super_categories = SuperCategory.objects.prefetch_related('category_set__subcategory_set').all()

    data = {
        "super_categories": []
    }

    for super_category in super_categories:
        super_category_data = {
            "name": super_category.name,
            "is_active": super_category.is_active,
            "image_url": super_category.image.url if super_category.image else None,
            "categories": []
        }

        for category in super_category.category_set.all():
            category_data = {
                "name": category.name,
                "sub_categories": []
            }

            for sub_category in category.subcategory_set.all():
                sub_category_data = {"name": sub_category.name}
                category_data["sub_categories"].append(sub_category_data)

            super_category_data["categories"].append(category_data)

        data["super_categories"].append(super_category_data)

    # Convert the final_data list to a JSON object
    drop_down_data = data

    # Now you can access and use json_data as a JSON object
    return render(request, 'customer/customer_landing.html',{'drop_down_data':drop_down_data})

def product(request, **kwargs):
    return render(request, 'customer/product.html')

def product_display(request, **kwargs):
    return render(request, 'customer/customer_home.html')