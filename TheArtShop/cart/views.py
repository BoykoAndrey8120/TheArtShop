from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from site_content.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    print(f'product_id {product_id}')
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    print(cart)
    return render(request, 'cart/detail.html', {'cart': cart})



# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
# from django.shortcuts import render, get_object_or_404, redirect
# from django.template.context_processors import request
#
# from .forms import OrderItemForm
# # from .models import Order, Cart, OrderItem, CartItem
# # from site_content.models import Product
#
#
# user = User

# def view_cart(request):
#     # Получаем корзину из сессии
#     cart = request.session.get('cart', {})
#
#     # Преобразуем данные для передачи в шаблон
#     # cart_items = [{'id': id, 'details': 'details'} for id, details in cart.items()]
#
#     return render(request, 'cart/cart.html', {'cart_items': cart})
#
#
# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#
#     # Получаем или создаем заказ для текущего пользователя
#     order, created = Order.objects.get_or_create(user=request.user)
#
#     # Получаем или создаем корзину для текущего пользователя
#     cart, created = Cart.objects.get_or_create(user=request.user)
#
#     # Проверяем, есть ли уже такой товар в корзине
#     order_item, order_item_created = OrderItem.objects.get_or_create(order=order, product=product)
#
#     if not order_item_created:
#         # Если товар уже есть в корзине, увеличиваем количество
#         order_item.quantity += 1
#         order_item.save()
#
#     # Если у заказа нет привязанной корзины, привязываем ее к текущей корзине
#     if not order.cart:
#         order.cart = cart
#         order.save()
#
#     return redirect('cart:cart')
#
#
# @login_required
# def checkout(request):
#     # Получаем или создаем заказ для текущего пользователя
#     order, created = Order.objects.get_or_create(user=request.user)
#
#     # Получаем или создаем корзину для текущего пользователя
#     cart, created = Cart.objects.get_or_create(user=request.user)
#
#     # Связываем корзину с заказом
#     order.cart = cart
#     order.save()
#
#     # Получаем или создаем элемент заказа для товаров в корзине
#     order_items = OrderItem.objects.filter(order=order)
#
#     if request.method == 'POST':
#         form = OrderItemForm(request.POST)
#         if form.is_valid():
#             for order_item in order_items:
#                 product_id = order_item.product.id
#                 quantity_key = f'quantity_{product_id}'
#                 if quantity_key in form.cleaned_data:
#                     order_item.quantity = form.cleaned_data[quantity_key]
#                     order_item.save()
#
#             # Очищаем корзину после оформления заказа
#             order_items.delete()
#
#             # Добавляем флеш-сообщение об успешном оформлении заказа
#             messages.success(request, 'Заказ успешно оформлен. Спасибо за покупку!')
#
#             # После успешного оформления заказа, редиректим на страницу корзины
#             return redirect('cart:checkout')  # Перенаправляем на ту же страницу для обновления данных
#
#     total_order_price = sum(item.total_price() for item in order_items)
#     form = OrderItemForm()
#
#     return render(request,
#                   'cart/checkout.html',
#                   {
#                       'order_items': order_items,
#                       'total_order_price': total_order_price,
#                       'form': form,
#                       # 'quantity': quantity
#                   })

