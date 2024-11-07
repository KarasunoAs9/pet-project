from django.db import models
from store.models import Product
from app_auth.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    image = models.ImageField(upload_to="reviews/")
    comment = models.TextField(max_length=2000)
    addet_to = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    