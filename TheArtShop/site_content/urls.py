from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import CategoryViews, ProductsViews, ProductView, Home


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("<slug:slug_category>", CategoryViews.as_view(), name="Category-detail"),
    path("<slug:slug_category>/products/page/<int:page>/", ProductsViews.as_view(), name='product-list-paginated'),
    path("<slug:slug_category>/products/", ProductsViews.as_view(), name="category_products",
         kwargs={'template_name': 'category_products.html'}),
    path("<slug:slug_category>/<slug:slug_product>/<int:pk>/", ProductView.as_view(), name='product_detail'),
    path("<slug:slug_category>/<slug:slug_product>/", ProductsViews.as_view(), name="product"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
