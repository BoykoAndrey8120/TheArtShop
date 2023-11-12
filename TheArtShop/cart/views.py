from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.context_processors import request
from .models import Order, Cart, OrderItem

user = User

# Create your views here.


@login_required
def cart_view(request):
    # order = request.order
    # l_user = request.user
    # product = request.product
    # context = {'order': order, 'user': l_user, 'product': product}
    context = {'test': 'test'}
    return render(request, 'cart/cart.html', context=context)


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, Order
from .forms import OrderItemForm

@login_required
def add_to_cart(request, product_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = Order.objects.filter(cart=cart)

    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            # product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']

            # Добавление товара в корзину
            cart_item, cart_item_created = OrderItemForm.objects.get_or_create(cart=cart, product_id=product_id)

            if not cart_item_created:
                cart_item.quantity += quantity
                cart_item.save()

            return redirect('cart')
    else:
        form = OrderItemForm()

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'form': form})


@login_required
def checkout(request):
    # Получаем или создаем заказ для текущего пользователя
    order, created = Order.objects.get_or_create(user=request.user)

    # Получаем или создаем элемент заказа для товаров в корзине
    order_items = OrderItem.objects.filter(order=order)

    if request.method == 'POST':
        # Обработка данных из формы, если необходимо
        # ...

        # Очистка корзины после оформления заказа
        order_items.delete()

        return redirect('success_page')  # Перенаправление на страницу успешного оформления заказа

    total_order_price = sum(item.total_price() for item in order_items)

    return render(request, 'cart/checkout.html', {'order_items': order_items, 'total_order_price': total_order_price})






