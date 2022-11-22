from django.shortcuts import render, redirect
# from .models import Item, Inventory

# Create your views here.


def home(request):
    return render(request, 'home.html')


def gloves(request):
    return render(request, 'ax/gloves.html')


def hats(request):
    return render(request, 'ax/hats.html')


def scarves(request):
    return render(request, 'ax/scarves.html')


def boots(request):
    return render(request, 'clothes/boots.html')


def jackets(request):
    return render(request, 'clothes/jackets.html')


def pants(request):
    return render(request, 'clothes/pants.html')


def shirts(request):
    return render(request, 'clothes/shirts.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
