from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomerRegistrationForm, UserLoginForm, EditCustomerForm
from django.contrib.auth import login, authenticate
from .models import Customer
from django.contrib.auth.models import User

class LoginCustomer(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "app_auth/login.html", {"form": form})
    
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
            
        return render(request, "app_auth/login.html", {"form": form})

class RegisterCustomer(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, "app_auth/register.html", {"form": form})
    
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
        
        return render(request, "app_auth/register.html", {"form": form})
    

class ProfilePage(View):
    def get(self, request):
        return render(request, "app_auth/profile.html")
    
class AccountEdit(View):
    def get(self, request):
        customer = request.user.customer
        form = EditCustomerForm(instance=customer, user=request.user)
        return render(request, "app_auth/account_edit.html", {"form": form})
    
    def post(self, request):
        customer = request.user.customer
        form = EditCustomerForm(request.POST, instance=customer, user=request.user)
        if form.is_valid():
            
            user = self.request.user
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            
            if form.cleaned_data["password"]:
                user.set_password(form.cleaned_data["password"])
            user.save()
            
            
            customer.user = user
            customer.email = form.cleaned_data["email"]
            customer.name = form.cleaned_data["name"]
            customer.last_name = form.cleaned_data["last_name"]
        
            customer.save()
            
            login(request, user)
            
            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        return render(request, "app_auth/account_edit.html", {"form": form})