from django.db import models

# Create your models here.


class Category(models.Model):
    title_category = models.CharField(max_length=255)
    slug_category = models.SlugField(max_length=100, db_index=True, unique=True)
    image_category = models.ImageField(upload_to='image/categories/', blank=True)

    class Meta:
        ordering =('title_category',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Brand(models.Model):
    title_brand = models.CharField(max_length=255)
    slug_brand = models.SlugField(max_length=100, db_index=True, unique=True)
    image_brand = models.ImageField(upload_to='image/brands/', blank=True)


class Product(models.Model):
    title_product = models.CharField(max_length=255)
    description_product = models.TextField(max_length=1000, blank=True)
    slug_product = models.SlugField(max_length=100, db_index=True, unique=True)
    price_product = models.DecimalField(max_digits=10, decimal_places=2)
    image_product = models.ImageField(upload_to='image/products/', blank=True)
    category_product = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    created = models.DateField(auto_now=True)
    brand_product = models.ForeignKey(Brand, related_name='product', on_delete=models.CASCADE)
    uploaded = models.DateField(auto_now=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('title_product', )
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug_product'), )

    def __str__(self):
        return self.title_product




