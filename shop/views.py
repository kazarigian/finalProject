from django.shortcuts import render, redirect
# from .models import Item, Inventory

# Create your views here.


def home(request):
    # item_list = Item.objects.all()
    return render(request, 'home.html')


def ax(request):
    # item_list = Item.objects.all()
    return render(request, 'ax.html')


def clothes(request):
    return render(request, 'clothes.html')


def boots(request):
    return render(request, 'boots.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
