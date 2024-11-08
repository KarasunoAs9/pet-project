from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from . import models
from django.views import View
from django.contrib.auth.decorators import login_required
from shopping.models import Cart
from django.utils.decorators import method_decorator
from app_auth.models import Customer

# Create your views here.

class MainPage(ListView):
    model = models.Product
    template_name = "store/main_page.html"
    context_object_name = "products"
    ordering = ["-addet_to"]
    paginate_by = 3

class ProductPage(DetailView):
    model = models.Product
    template_name = "store/product_page.html"
    context_object_name = "product"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug  = self.kwargs.get("slug")
        product = models.Product.objects.get(slug=slug)
        similar_products = models.Product.objects.filter(category=product.category).exclude(id=product.id)
        context["similar_products"] = similar_products
        if len(product.reviews.all()) > 0:
            rating = sum([i.rating for i in product.reviews.all()]) // len(product.reviews.all())
        else:
            rating = 0
        context["rating_num"] = rating
        context["rating"] = range(1, 6)

        return context
    
    
@method_decorator(login_required, name='dispatch')   
class AddToCart(View):
    def post(self, request):
        req_id = request.POST.get("product_id")
        req_size = request.POST.get("size_id")
        
        user = get_object_or_404(Customer, user=self.request.user) 
        
        product = get_object_or_404(models.Product, pk=req_id)
        size = get_object_or_404(models.ProductSize, pk=req_size, product=product)
        
        cart, created = Cart.objects.get_or_create(
            user = user,
            product = product,
            size = size,
        )
        
        if not created:
            cart.quantity += 1
            cart.save()
        
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
class ShopPage(ListView):
    model = models.ProductCategory
    template_name = "store/shop_page.html"
    context_object_name = "categorys"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get("search", "")
        if search_query:
            context["products"] = models.Product.objects.filter(name__icontains=search_query)
        else:    
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

class About(View):
    def get(self, request):
        return render(request, "store/about_page.html")