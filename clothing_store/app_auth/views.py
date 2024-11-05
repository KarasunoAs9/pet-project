from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate

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
            customer = form.save()
            login(request, customer.user)
            return redirect("main-page")
        
        return render(request, "app_auth/register_page.html", {"form": form})
    
    
class CustomerProfile(View):
    pass