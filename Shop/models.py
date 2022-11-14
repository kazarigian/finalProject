from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    class Meta:
        def __str__(self):
            return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_maker')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    stock = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    price = models.SlugField(max_length=6)

    class Meta:
        ordering =('-created',)

        def __str__(self):
            return self.title

