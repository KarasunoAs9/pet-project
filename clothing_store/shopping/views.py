from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import Cart, Orders
from app_auth.models import Customer
from django.views import View
from django.http import JsonResponse
from .forms import PaymentForm
import json

# Create your views here.
class CartView(ListView):
    model = Cart
    template_name = "shopping/cart.html"
    context_object_name = "products"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = Customer.objects.get(user=self.request.user)
        cart = Cart.objects.filter(user=customer)
        form = PaymentForm()
        context["total_sum"] = sum([i.product.price * i.quantity for i in cart])
        
        for item in cart:
            max_quantity = min(item.size.quantity, 10)
            item.quantity_range = range(1, max_quantity + 1)
        
        context["cart_items"] = cart
        context["form"] = form
        return context


class UpdateQuantity(View):
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        cart_id = int(data.get("cart_id"))
        quantity = int(data.get("quantity", 1))
        
        try:
            cart_item = Cart.objects.get(pk=cart_id)
            cart_item.quantity = quantity
            cart_item.save()
            
            customer = Customer.objects.get(user=self.request.user)
            cart = Cart.objects.filter(user=customer)
            total_sum = sum([i.product.price * i.quantity for i in cart])
            
            return JsonResponse({"success":True, "total_sum": total_sum})
          
        except Cart.DoesNotExist:
            return JsonResponse({"succes": False, "error": "Item not found"})
        

class DeleteProduct(View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = Cart.objects.get(pk=cart_id)
        cart.delete()
        return redirect(request.META.get('HTTP_REFERER', '/'))
    
    
class CreateOrder(View):
    def post(self, request):
        form = PaymentForm(request.POST)
        
        cart_items = request.POST.get("cart_items")
        cart_id = list(map(int, cart_items.split()))
        cart_obj = Cart.objects.filter(id__in=cart_id)
        user = Customer.objects.get(user=self.request.user)
        total_sum = request.POST.get("total_sum")
           
        order = Orders.objects.create(user=user, total_sum=total_sum)
        order.created_order_item(cart_obj)
        cart_obj.delete()
             
        return redirect("profile")

        
        
    
       