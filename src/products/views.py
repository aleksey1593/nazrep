from django.shortcuts import render
from products.models import *
from core.settings import BASE_DIR
from django.db.models import Max


def product(request, product_id):
    product = Product.objects.get(id=product_id)
    max_id = Product.objects.aggregate(Max('id'))
    latest_product = Product.objects.get(id=max_id['id__max'])

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    return render(request, f'{BASE_DIR}/src/products/templates/product.html', locals())
