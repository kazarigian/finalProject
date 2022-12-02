from django.db import models
from django.contrib.auth.models import User

# Create your models here.
colors = (
    ('Blue', 'blue'),
    ('White', 'white'),
    ('Black', 'black'),
    ('Grey', 'grey'),
    ('Purple', 'purple'),
    ('Green', 'green'),
    ('Red', 'red'),
)
types = (
    ('Shirt', 'shirt'),
    ('Coat', 'coat'),
    ('Scarves', 'scarves'),
    ('Boots', 'boots'),
    ('Gloves', 'gloves'),
    ('Hats', 'hats'),
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    type = models.CharField(max_length=50, choices=types, null=True)
    color = models.CharField(max_length=10, choices=colors, null=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    items = models.ManyToManyField(Item)
    quantity = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # one to many
    purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class Checkout(models.Model):
    cart = models.ManyToManyField(Cart)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
