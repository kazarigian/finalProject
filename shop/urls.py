from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('clothes/', views.clothes, name='clothes'),
    path('boots/', views.boots, name='boots'),
    path('ax/', views.ax, name='ax'),
    path('cart/', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout')
]
