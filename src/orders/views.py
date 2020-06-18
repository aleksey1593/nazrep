from django.http import JsonResponse
from .models import *
from core.settings import BASE_DIR
from django.shortcuts import render
from .forms import CheckoutContactForm
from django.contrib.auth.models import User
from django.db.models import Max
from django.http import HttpResponseRedirect


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    nmb = data.get("nmb")
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInBasket.objects.get_or_create(session_key=session_key, product_id=product_id,
                                                                     is_active=True, defaults={"nmb": nmb})
        if not created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb

    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    max_id = Product.objects.aggregate(Max('id'))
    latest_product = Product.objects.get(id=max_id['id__max'])
    products_in_basket = ProductInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = CheckoutContactForm(request.POST or None)
    data = request.POST
    if data:
        if form.is_valid():
            phone = data["phone"]
            address = data["address"]
            name = data.get("name", "1111111")
            user, created = User.objects.get_or_create(username=phone, defaults={"first_name": name})
            order = Order.objects.create(user=user, customer_name=name, customer_phone=phone, customer_address=address, status_id=1)
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductInBasket.objects.get(id=product_in_basket_id)

                    product_in_basket.nmb = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_basket.product, nmb=product_in_basket.nmb,
                                                  price_per_item=product_in_basket.price_per_item,
                                                  total_price=product_in_basket.total_price,
                                                  order=order)
                    return HttpResponseRedirect('/checkout/thanks/')


    return render(request, f'{BASE_DIR}/src/orders/templates/checkout.html', locals())


def checkout_thanks(request):
    return render(request, f'{BASE_DIR}/src/orders/templates/checkout_apply.html', locals())