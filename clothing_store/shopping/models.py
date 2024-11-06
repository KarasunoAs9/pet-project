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
    number = models.PositiveBigIntegerField(unique=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES)
    cart = models.ManyToManyField(Cart, related_name="cart")
    added_to = models.DateTimeField(auto_now_add=True)
    
    
    def save(self, *args, **kwargs):
        if not self.number:
            random.randint(10000, 99999)
        
        while Orders.objects.filter(number=self.number).exists():
            self.number = random.randint(10000, 99999)        
        
        super().save(*args, **kwargs)

class Payment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    cart_number = models.CharField(max_length=19)
    expiration_term = models.CharField(max_length=5)
    cvv = models.PositiveIntegerField()
    
    
    
    
    