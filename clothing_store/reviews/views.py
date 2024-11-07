from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Review
from django.views import View
from app_auth.models import Customer
from store.models import Product
from .form import ReviewsForm

# Create your views here.
class ReveiwsPage(View):
    def get(self, request, slug):
        form = ReviewsForm()
        product = Product.objects.get(slug=slug)
        reviews = Review.objects.filter(product=product).order_by("-addet_to")
        return render(request, "reviews/reviews.html", 
                      {"form": form, 
                       "reviews": reviews, 
                       "product": product,
                       "rating": range(1, 6)
                       })
    
    def post(self, request, slug):
        product = Product.objects.get(slug=slug)
        form = ReviewsForm(request.POST)
        customer = Customer.objects.get(user=self.request.user)
        
        if form.is_valid():
            Review.objects.create(
                user = customer,
                product = product,
                rating = form.cleaned_data["rating"],
                comment = form.cleaned_data["comment"]
            )

            return redirect(request.META.get('HTTP_REFERER', '/'))
        
        return render(request, "reviews/reviews.html", {"form": form})

    