# from django.contrib.auth.models import User
# from django.db import models
#
# from site_content.models import Product
#
#
# # Create your models here.
#
#
# from django.contrib.auth.models import User
# from django.db import models
#
# from site_content.models import Product


# class Order(models.Model):
#     user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, related_name='orders', through='OrderItem')
#
#     def __str__(self):
#         return f"Order {self.id} by {self.user.username}"
#
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} in Order"
#
#
# class Cart(models.Model):
#     order = models.ForeignKey(Order, related_name='carts', on_delete=models.CASCADE)
#
# # class CartItem(models.Model):
# #     cart = models.ForeignKey('Cart', related_name='items', on_delete=models.CASCADE)
# #     product = models.ForeignKey(Product, related_name='cart_items', on_delete=models.CASCADE)
# #     quantity = models.PositiveIntegerField(default=1)
# #
# #     def __str__(self):
# #         return f"{self.quantity} x {self.product.name} in Cart"
# #
# #     def total_price(self):
# #         return self.quantity * self.product.price

from django.contrib.auth.models import User
from django.db import models


# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def __str__(self):
#         return f"{self.quantity} x {self.product.name} в корзине"
#
#     def total_price(self):
#         return self.quantity * self.product.price
#
#
#
#
#
#

#
# class Order(models.Model):
#     user = models.ForeignKey(User, related_name="orders", on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderItem')
#     cart = models.ForeignKey(Cart, related_name="orders", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"Заказ {self.id} от {self.user.username}"
#
# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#
#     def total_price(self):
#         return self.quantity * self.product.price_product
#
#     def __str__(self):
#         return f"{self.quantity} x {self.product.title_product} в заказе"
#
#     def __str__(self):
#         return f"{self.quantity} x {self.product.title_product} в заказе"
#

