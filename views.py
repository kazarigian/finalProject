from django.shortcuts import render, redirect
from .models import Item, Checkout

# Create your views here.

# context = {'items': Item.objects.all()}


def home(request):
    return render(request, 'home.html')


def gloves(request):
    item_list = Item.objects.filter(type__icontains='gloves')
    context = {'items': item_list}
    return render(request, 'ax/gloves.html', context)


def hats(request):
    item_list = Item.objects.filter(type__icontains='hats')
    context = {'items': item_list}
    return render(request, 'ax/hats.html', context)


def scarves(request):
    item_list = Item.objects.filter(type__icontains='scarves')
    context = {'items': item_list}
    return render(request, 'ax/scarves.html', context)


def boots(request):
    item_list = Item.objects.filter(type__icontains='boot')
    context = {'items': item_list}
    return render(request, 'clothes/boots.html', context)


def coats(request):
    item_list = Item.objects.filter(type__icontains='coat')

    context = {'items': item_list}
    return render(request, 'clothes/coats.html', context)


def shirts(request):
    item_list = Item.objects.filter(type__icontains='shirt')
    context = {'items': item_list}
    return render(request, 'clothes/shirts.html', context)


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def item(request):
    return render(request, 'item.html')

