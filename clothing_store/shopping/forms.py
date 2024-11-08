from django import forms
from .models import Orders
from datetime import datetime
from django.core.exceptions import ValidationError

def clean_expiration_term(value):
        try:
            datetime.strptime(value, "%m/%y")
        except ValueError:
            raise ValidationError("Enter date")

        month, year = map(int, value.split("/"))
        if not (1 <= month <= 12):
            raise ValidationError("Unexpected month")
        
        current_date = datetime.now()
        expiration_date = datetime.strptime(value, "%m/%y")
        
        if expiration_date < current_date:
            raise ValidationError("Expiry date of the leak card.")
        
        return value
class PaymentForm(forms.Form):
    cart_number = forms.CharField(
        max_length=19,min_length=13 ,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "XXXX XXXX XXXX XXXX"})
        )
    
    expiration_term = forms.CharField(max_length=5, required=True, 
                                      widget=forms.TextInput(attrs={"placeholder": "MM/YY"}), 
                                      min_length=5, validators=[clean_expiration_term])
    cvv = forms.CharField(min_length=3, max_length=3, required=True, widget=forms.TextInput(attrs={"placeholder": "000"}))