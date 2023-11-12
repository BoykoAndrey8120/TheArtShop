from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import LogoutView, LoginView
from users.views import (CustomLoginView, CustomLogoutView, register)
from .views import CategoryViews, ProductsViews, ProductView, Home


urlpatterns = [
    # path('register/', register, name='register'),
    # path("login/", CustomLoginView.as_view(), name='login'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('logout/', CustomLogoutView.as_view(), name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path("", Home.as_view(), name="home"),
    path("<slug:slug_category>/", CategoryViews.as_view(), name="Category-detail"),
    path("<slug:slug_category>/products/page/<int:page>/", ProductsViews.as_view(), name='product-list-paginated'),
    path("<slug:slug_category>/products/", ProductsViews.as_view(), name="category_products", kwargs={'template_name': 'category_products.html'}),
    path("<slug:slug_category>/<slug:slug_product>/<int:pk>/", ProductView.as_view(), name='product_detail'),
    path("<slug:slug_category>/<slug:slug_product>/", ProductsViews.as_view(), name="product"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns = [
#     #your url
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)