from django import forms
from .models import Customer
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128, required=True)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput, required=True)

class CustomerRegistrationForm(forms.ModelForm):
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
        
        
class EditCustomerForm(forms.ModelForm):
    username = forms.CharField(max_length=128, required=False)
    password = forms.CharField(max_length=128,widget=forms.PasswordInput, required=False)
    email = forms.EmailField(max_length=128, required=False)
    name = forms.CharField(max_length=128, required=False)
    last_name = forms.CharField(max_length=128, required=False)
    class Meta:
        model = Customer
        fields = ["email", "name", "last_name"]
    
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super(EditCustomerForm, self).__init__(*args, **kwargs) 
        if user:
            self.fields["username"].initial = user.username
    
    def save(self, commit=True):
        customer = super().save(commit=False)
        user = customer.user
        
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
            
        if commit:
            user.save()
            customer.save()
            
        return customer
        
        
        
    