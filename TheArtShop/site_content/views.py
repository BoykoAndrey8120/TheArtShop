from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def home(request):
    list_category = Category.objects.all()
    list_product = Product.objects.all()

    template = loader.get_template('site_content/base.html')
    context = {
        'list_product': list_product,
        'list_category': list_category
    }
    # return HttpResponse('<p>Пример</p>')
    return HttpResponse(template.render(context, request))

