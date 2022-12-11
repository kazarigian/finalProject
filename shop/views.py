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


def coats(request):
    return render(request, 'clothes/coats.html')


def shirts(request):
    return render(request, 'clothes/shirts.html')


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')

def weather(request):
    ## if request.method == 'POST':
    ##  check = request.POST.get('Check')
    ## location = request.POST.get('location')

    url = 'http://api.weatherapi.com/v1/current.json?key=2a5e5b2bcf3d4eda880192423221012&q=Hartford&aqi=yes'
    response = requests.get(url)
    data = response.json()
    print(data)
    context = {"data": data}
    return render(request, 'weather.html', context)
