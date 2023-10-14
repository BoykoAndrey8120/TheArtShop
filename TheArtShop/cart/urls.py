from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import cart_view, add_to_cart, checkout


app_name = 'cart'

urlpatterns = [
    path('/order/', cart_view, name='cart'),
    path('/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
