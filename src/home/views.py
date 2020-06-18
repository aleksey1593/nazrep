from platform import system
from django.shortcuts import render
from products.models import *
from django.db.models import Max


def index(request, **slug):
    if slug:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__category__id=slug["slug"])
    else:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, "main.html", locals())

def discount_products(request):

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True, product__discount__gt=0)

    return render(request, "main.html", locals())

def delivery(request):

    max_id = Product.objects.aggregate(Max('id'))
    latest_product = Product.objects.get(id=max_id['id__max'])

    return render(request, "dostavka.html", locals())

def info_shop(request):

    max_id = Product.objects.aggregate(Max('id'))
    latest_product = Product.objects.get(id=max_id['id__max'])

    return render(request, "info_magazin.html", locals())
