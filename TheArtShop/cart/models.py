from django.contrib.auth.models import User
from django.db import models

from site_content.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, related_name="заказы", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='заказы', on_delete=models.CASCADE)
    number_of_order = models.IntegerField(unique=True)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        if not self.number_of_order:
            last_order = Order.objects.filter(user=self.user).order_by('-number_of_order').first()
            if last_order:
                self.number_of_order = last_order.number_of_order + 1
            else:
                self.number_of_order = 1

class Cart(models.Model):
    oder = models.ForeignKey(Order, related_name='Заказ', on_delete=models.CASCADE)


