from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('home/', views.home, name='home'),
    path('boots/', views.boots, name='boots'),
    path('coats/', views.coats, name='coats'),
    path('shirts/', views.shirts, name='shirts'),
    path('gloves/', views.gloves, name='gloves'),
    path('hats/', views.hats, name='hats'),
    path('scarves/', views.scarves, name='scarves'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('item/<int:item_id>', views.product_details, name='item'),
    path('aboutus/', views.aboutus, name='aboutus')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  <int:quantity_num>
