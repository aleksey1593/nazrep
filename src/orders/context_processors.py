from .models import ProductInBasket
from products.models import *


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    products_total_nmb = products_in_basket.count()

    return locals()


def category(request):
    categories = Category.objects.filter(is_active=True)
    even = []
    for nmb in range(categories.count()+1):
        if nmb and nmb % 2 == 0:
            even.append(nmb)
    return locals()
