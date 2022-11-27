from django.db import models

# Create your models here.
colors = (
    ('Blue', 'blue'),
    ('White', 'white'),
    ('Black', 'black'),
    ('Grey', 'grey'),
)


class Category(models.Model):
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=10, choices=colors)


class Item(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    #   image = models.ImageField()
    stock = models.BooleanField()
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    Item = models.ManyToManyField(Item)
    quantity = models.IntegerField()


class Customer(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=10)
    email = models.EmailField()


class Cart(models.Model):
    items = models.ManyToManyField(Item)
    customer = models.ManyToManyField(Customer)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
