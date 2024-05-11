from django.views.generic import ListView, DetailView
from .models import Product, Category
from cart.forms import CartAddProductForm


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

    def get_queryset(self):
        category_slug = self.kwargs['slug_category']
        category = Category.objects.get(slug_category=category_slug)
        return Product.objects.filter(category_product=category, available=True)


class ProductView(DetailView):
    template_name = 'site_content/product.html'
    model = Product
    context_object_name = 'product'
