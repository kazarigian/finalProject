from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth. decorators import login_required

# Create your views here.


@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'accounts/index.html')


def register_view(request):
    form = UserCreationForm(request.POST or None)
    # check whether post or not, if post they clicked the register button
    if request.method == 'POST':
        if form.is_valid():  # checks whether fields are filled and meet qualifications (ex passoword qualifications)
            form.save()
            return redirect('index')
    else:
        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def login_view(request):
    form = AuthenticationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            # get user info from form
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        context = {'form': form}
        return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')