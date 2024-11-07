from django.db import models
from app_auth.models import Customer
from store.models import Product, ProductSize
from django.core.validators import MaxValueValidator
import random


class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=1)
    added_to = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.size.name } for {self.user}"
    
    
class Orders(models.Model):
    STATUS_CHOICES = [
        ("In progres", "In progres"),
        ("Delivery", "Delivery"),
        ("Completed", "Completed")
    ]
    
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    number = models.PositiveBigIntegerField(unique=True, null=True, blank=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="In progres")
    total_sum = models.PositiveBigIntegerField(default=0)
    added_to = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        if not self.number:
            self.number = random.randint(10000, 99999)
        
        while Orders.objects.filter(number=self.number).exists():
            self.number = random.randint(10000, 99999)        
        
        super().save(*args, **kwargs)
        
        
    def created_order_item(self, cart_items):
        for cart_item in cart_items:
            OrderItem.objects.get_or_create(
                order = self,
                product = cart_item.product,
                size = cart_item.size,
                quantity = cart_item.quantity,
            )
            


class OrderItem(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="order")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=4)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=1)
    added_to = models.DateTimeField(auto_now_add=True)

    
    
    
    