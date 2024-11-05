from django import forms
from .models import Customer
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput, required=True)

class CustomerRegistrationForm(forms.Form):
    username = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput, required=True)
    email = forms.EmailField(max_length=128, required=True)
    name = forms.CharField(max_length=128, required=True)
    last_name = forms.CharField(max_length=128, required=True)
    
    class Meta:
        model = Customer
        fields = ["username", "password", "email", "name", "last_name"]
        
    def save(self, commit=True):
        user = User(
            username = self.cleaned_data["username"],
            password = self.cleaned_data["password"]
        )
        
        customer = Customer(
            user=user,
            email = self.cleaned_data["email"],
            name = self.cleaned_data["name"],
            last_name = self.cleaned_data["last_name"],
        )
        
        if commit:
            user.save()
            customer.save()
            
        return customer
        
        
    
    