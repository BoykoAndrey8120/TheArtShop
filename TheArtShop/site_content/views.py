from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.core.paginator import Paginator, Page
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Product, Category


class Home(ListView):
    model = Category
    paginate_by = 10
    template_name = 'site_content/home.html'
    context_object_name = 'list_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        is_homepage = True
        return context


class CategoryViews(DetailView):
    template_name = 'site_content/category.html'
    model = Category
    context_object_name = 'category'

    def get_object(self, queryset=None):
        return Category.objects.get(slug_category=self.kwargs['slug_category'])


class ProductsViews(ListView):
    model = Product
    paginate_by = 50
    template_name = 'site_content/products.html'
    context_object_name = 'list_products'

class CustomLoginView(LoginView):
    template_name = 'site_content/login.html'
    success_url = 'home'


class CustomLogoutView(LogoutView):
    template_name = 'site_content/logout.html'
    # next_page = reverse_lazy('home')

    def get_queryset(self):
        category_slug = self.kwargs['slug_category']
        category = Category.objects.get(slug_category=category_slug)
        return Product.objects.filter(category_product=category, available=True)


def category_with_products_list(request, slug_category, slug_product, template_name):
    # Ваш код для обработки запроса
    category = Category.objects.get(slug_category=slug_category)
    products = Product.objects.filter(category_product=category)
    return render(request, 'site_content/category_products.html', {'category': category, 'products': products})


class ProductView(DetailView):
    template_name = 'site_content/product.html'
    model = Product
    context_object_name = 'product'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически войдите в систему после регистрации
            return redirect('home')  # Замените 'home' на URL-маршрут вашей домашней страницы
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



