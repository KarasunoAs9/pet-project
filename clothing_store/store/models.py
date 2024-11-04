from django.db import models
from django.utils.text import slugify

class ProductCategory(models.Model):
    SEX_CHOICES = [
        ("Female", "Female"),
        ("Male", "Male"),
        ("Unisex", "Unisex")
    ]
    
    name = models.CharField(max_length=50)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    
    slug_name =  models.SlugField(null=True, blank=True)
    slug_sex = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug_name and not self.slug_sex:
            self.slug_name = slugify(self.name)
            self.slug_sex = slugify(self.sex)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
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
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    
    def __str__(self):
        return self.size
    
