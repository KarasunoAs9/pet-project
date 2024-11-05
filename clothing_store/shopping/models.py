from django.db import models
from app_auth.models import Customer
from store.models import Product, ProductSize
from django.core.validators import MaxValueValidator

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(ProductSize, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MaxValueValidator(10)], default=1)
    added_to = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.size.name } for {self.user}"