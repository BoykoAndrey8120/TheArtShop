from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.template.context_processors import request
from .models import Order, Cart

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









