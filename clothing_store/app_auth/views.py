from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate
from .models import Customer
from django.contrib.auth.models import User

class LoginCustomer(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "app_auth/login_page.html", {"form": form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect("main-page")
            else:
                form.add_error(None, "Invalid username or password")
            
        return render(request, "app_auth/login_page.html", {"form": form})

class RegisterCustomer(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app_auth/register_page.html", {"form": form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            user = User(username=form.cleaned_data["username"], email=form.cleaned_data["email"])
            user.set_password(form.cleaned_data["password"])
            user.save()
            
            customer = Customer(user=user, email=form.cleaned_data["email"], name=form.cleaned_data["name"], last_name=form.cleaned_data["last_name"])
            customer.save()
            
            login(request, user)
            return redirect("main-page")
        
        return render(request, "app_auth/register_page.html", {"form": form})
    
    
class CustomerProfile(View):
    pass