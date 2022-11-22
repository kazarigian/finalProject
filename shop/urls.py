from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    path('boots/', views.boots, name='boots'),
    path('jackets/', views.jackets, name='jackets'),
    path('pants/', views.pants, name='pants'),
    path('shirts/', views.shirts, name='shirts'),
    path('gloves/', views.gloves, name='gloves'),
    path('hats/', views.hats, name='hats'),
    path('scarves/', views.scarves, name='scarves'),
    path('cart/', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout')
]
