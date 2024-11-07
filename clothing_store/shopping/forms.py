from django import forms
from .models import Orders
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class PaymentForm(forms.Form):
    cart_number = forms.CharField(
        max_length=19,min_length=13 ,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "XXXX XXXX XXXX XXXX"})
        )
    expiration_term = forms.CharField(max_length=5, required=True, widget=forms.TextInput(attrs={"placeholder": "MM/YY"}))
    cvv = forms.CharField(min_length=3, max_length=3, required=True, widget=forms.TextInput(
        attrs={"placeholder": "000"}
    ))
    
    def clean_expiration_term(self):
        data = self.cleaned_data["expiration_term"]
        
        try:
            datetime.strptime(data, "%m/%y")
        except ValueError:
            raise forms.ValidationError("Enter date")
        
        current_date = datetime.now()
        expiration_date = datetime.strptime(data, "%m/%y")
        
        if expiration_date < current_date:
            raise forms.ValidationError("Expiry date of the leak card.")