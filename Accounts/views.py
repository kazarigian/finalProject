from django.shortcuts import render, redirect
from django.template import context

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Login Page
@login_required(login_url='accounts/Login.html')
def my_view(request):
    return render(request, 'accounts/index.html')

    # Used to Create Form with username and Password fields, authenticate user w/ login()


def register_view(request, data=None):
    if request.method == 'POST':
        form = AuthenticationForm(data.request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/Login.html', context, {'form': form})


# Log user out, takes HttpRequest Object
def logout_view(request):
    logout(request)

    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            return redirect('index')

    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


