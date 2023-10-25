from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import cart_view

urlpatterns = [
    path('/order/', cart_view, name='cart'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
