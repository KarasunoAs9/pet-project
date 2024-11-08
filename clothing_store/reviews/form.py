from django import forms
from .models import Review

class ReviewsForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5, min_value=1, required=True)
    class Meta:
        model = Review
        fields = ["rating", "comment"]