from .models import Category, Product, Brand
import random
from slugify import slugify


def generate_products(num_products=1000):
    categories = Category.objects.all()
    brands = Brand.objects.all()

    for _ in range(num_products):
        title = f"Product {_ + 1}"
        description = f"Description for Product {_ + 1}"
        price = round(random.uniform(1.0, 100.0), 2)
        image = None  # Здесь можно указать путь к изображению, если есть
        category = random.choice(categories)
        brand = random.choice(brands)

        slug = slugify(title)

        Product.objects.create(
            title_product=title,
            description_product=description,
            price_product=price,
            image_product=image,
            category_product=category,
            brand_product=brand,
            slug_product=slug  # Устанавливаем генерированный слаг
        )


def create_unique_slug(instance, new_slug=None):
    slug = new_slug or slugify(instance.title_product)
    qs = Product.objects.filter(slug_product=slug).exclude(id=instance.id)
    if qs.exists():
        new_slug = f"{slug}-{instance.id}"
        return create_unique_slug(instance, new_slug=new_slug)
    return slug


def save(self, *args, **kwargs):
    if not self.slug_product:
        self.slug_product = create_unique_slug(self)
    super().save(*args, **kwargs)
