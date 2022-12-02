from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Register(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    user = forms.CharField(required=True, label='Username')

    class Meta:
        model = User
        fields = ['username', 'password', 're-enter']
