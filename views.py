from django.shortcuts import render, redirect
from .models import Item, Cart

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


# def cart(request, user_id):
#     # return items in cart table that match user id ... this is returning cart objects(?)
#     cart_list = Cart.objects.get(id=user_id)
#     context = {'items': cart_list}
#     return render(request, 'cart.html', context)
def cart(request):
    return render(request, 'cart.html')




def add_to_cart(request, item_id, user_id):
    # how to add based on id,s or can we pass the actual item and cart objects somehow
    Cart.objects.create(items=item_id, user=user_id)
    return render(request)


def checkout(request):
    # for items in cart with user_id, change purchased to true
    return render(request, 'checkout.html')


def item(request):
    return render(request, 'item.html')


def product_details(request, item_id):
    # Get the product based on its id
    itemi = Item.objects.get(id=item_id)

    # render the page with the product's info
    return render(request, 'item.html', {'itemi': itemi})


def aboutus(request):
    return render(request, 'aboutus.html')
