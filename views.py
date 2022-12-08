from django.shortcuts import render, redirect
from .models import Item, Cart

# Create your views here.

# context = {'items': Item.objects.all()}


def home(request):
    return render(request, 'home.html')


def clothes(request, typ):
    search = typ
    item_list = Item.objects.filter(type__icontains=search)
    context = {'items': item_list, 'type': search}
    return render(request, 'item_template.html', context)


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
    if request.method == 'POST':
        ite = Cart.objects.filter(user=request.user).filter(items=request.POST['item_id'])
        ite.delete()
    # return items in cart table that match user id and are unpurchased
    my_cart = Item.objects.filter(cart__user=request.user).filter(cart__purchased=False)
    context = {'items': my_cart}
    return render(request, 'cart.html', context)


def checkout(request):
    # for items in cart with user_id, change purchased to true
    # add POST stuff
    if request.method == 'POST':
        items_cart = Cart.objects.filter(user=request.user)
        for items in items_cart:
            items.purchased = True
            items.save()
        return render(request, 'aboutus.html')

    return render(request, 'checkout.html')


def item(request, item_id):
    # if post then adding the item to the cart
    if request.method == 'POST':
        user_quantity = request.POST['quantity']
        o = Cart.objects.create(user=request.user)
        o.quantity = user_quantity
        o.items.add(item_id)
        o.purchased = False
        o.save()
        return redirect('cart')
    # Get the product based on its id
    itemi = Item.objects.get(id=item_id)

    # render the page with the product's info
    return render(request, 'item.html', {'itemi': itemi})


def aboutus(request):
    return render(request, 'aboutus.html')
