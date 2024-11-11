from django.db import models
from django.utils.text import slugify
import uuid

class ProductCategory(models.Model):
    SEX_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Unisex", "Unisex")
    ]
    
    name = models.CharField(max_length=50)
    sex = models.JSONField(default=list)
    
    slug_name =  models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug_name:
            self.slug_name = slugify(self.name)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    addet_to = models.DateTimeField(auto_now_add=True, null=True)
    
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_suffix = str(uuid.uuid4())[:8]
            self.slug = f"{self.slug}-{unique_suffix}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
class ProductImages(models.Model):
    image = models.ImageField(upload_to="images/")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    
class ProductSize(models.Model):
    SIZE_CHOICES = [
        ("XS", "XS"),
        ("S", "S"),
        ("M", "M"),
        ("L", "L"),
        ("XL", "XL"),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sizes")
    name = models.CharField(max_length=2, choices=SIZE_CHOICES)
    quantity = models.PositiveIntegerField(default=0)
    
    def in_stock(self):
        return self.quantity > 0
    
    def __str__(self):
        return self.name
