from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.conf.urls import url
from . import views
from .views import cart_add

# from .views import add_to_cart, view_cart, checkout


app_name = 'cart'

# urlpatterns = [
#     # path('cart_add/<int:product_id>/', cart_add, name='cart_add'),
#     # path('order/', view_cart, name='cart'),
#     # path('checkout/', checkout, name='checkout'),
#     path('cart/', views.cart_detail, name='cart_detail'),
#     path('cart_add/', views.cart_add, name='cart_add'),
#     # path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
#
# ]

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
]
# urlpatterns = [
#     path(r'^$', views.cart_detail, name='cart_detail'),
#     path(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
#     path(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
# ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
