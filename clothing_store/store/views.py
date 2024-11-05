from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from . import models

# Create your views here.

class MainPage(ListView):
    model = models.Product
    template_name = "store/main_page.html"
    context_object_name = "products"

class ProductPage(DetailView):
    model = models.Product
    template_name = "store/product_page.html"
    context_object_name = "product"
    
class ShopPage(ListView):
    model = models.ProductCategory
    template_name = "store/shop_page.html"
    context_object_name = "categorys"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = models.Product.objects.all() 
        return context

class CategoryPage(ListView):
    model = models.ProductCategory
    template_name = "store/shop_page.html"
    context_object_name = "categorys"
    
    def get_context_data(self, **kwargs):
        category_slug = self.kwargs.get("slug")
        category_object = models.ProductCategory.objects.get(slug_name=category_slug)
        context = super().get_context_data(**kwargs)
        context["products"] = models.Product.objects.filter(category=category_object)
        return context
    