# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .forms import RegistrationForm
# from django.contrib import messages
# from django.views.decorators.csrf import csrf_exempt


# from django.shortcuts import render, redirect
# from .forms import RegistrationForm


# @csrf_exempt
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(data=request.POST)
#         print(form.is_valid())
#         if form.is_valid():
#             if User.objects.filter(email=form.cleaned_data['email']).exists():
#                 messages.error(request, 'User already exists.')
#             else:
#                 form.save()
#                 return redirect('login')
#     else:
#         form = RegistrationForm()
#     return render(request, 'customer/register.html', {'form': form})


# @csrf_exempt
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         print("here",form.is_valid)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             print(email,password)

#             # Perform further validation or authentication logic
#             # ...
#             # If validation is successful, redirect the user
#             return redirect('home')  # Replace 'home' with your desired redirect URL
#     else:
#         form = LoginForm()
#     return render(request, 'customer/login.html', {'form': form})


from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout

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

def home(request, **kwargs):
    categories_content = "hello there"
    return render(request, 'customer/customer_landing.html', {'categories_content': categories_content})

def product(request, **kwargs):
    return render(request, 'customer/product.html')

def product_display(request, **kwargs):
    return render(request, 'customer/customer_home.html')