from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (CustomLoginView, CustomLogoutView, register)


urlpatterns = [
    path('register/', register, name='register'),
    path("login/", CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
               static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
