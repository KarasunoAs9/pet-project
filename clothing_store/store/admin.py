from django.contrib import admin
from . import models
from django import forms

class ProductCategoryForm(forms.ModelForm):
    sex = forms.MultipleChoiceField(
        choices=models.ProductCategory.SEX_CHOICES,
        widget= forms.CheckboxSelectMultiple,
        required=False
    )
    
    class Meta:
        model = models.ProductCategory
        fields = "__all__"
        
class ProductCategoryAdmin(admin.ModelAdmin):
    form = ProductCategoryForm

admin.site.register(models.Product)
admin.site.register(models.ProductSize)
admin.site.register(models.ProductCategory, ProductCategoryAdmin)
admin.site.register(models.ProductImages)