from core.settings import BASE_DIR
from django.shortcuts import render
from django.db.models import Q
from products.models import *


def search(request):
    search = request.GET.get('search', '')
    if search:
        products_images = ProductImage.objects.filter(Q(product__name__icontains=search) | Q(product__description__icontains=search) | Q(product__category__name__icontains=search),
                                                      Q(is_active=True),
                                                      Q(is_main=True),
                                                      Q(product__is_active=True)
                                                      )
    else:
        products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)

    return render(request, f'{BASE_DIR}/src/home/templates/main.html', locals())
