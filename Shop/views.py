from django.shortcuts import render
from .models import Product


def contact(request):
    form = Product(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'Product/Home.html')
    context = {'form': form}
    return render(request, 'Product/Buy.html', context)


# Create your views here.
