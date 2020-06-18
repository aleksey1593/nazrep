from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class Statusadmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, Statusadmin)


class Orderadmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]
    class Meta:
        model = Order

admin.site.register(Order, Orderadmin)


class ProductInOrderadmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder

admin.site.register(ProductInOrder, ProductInOrderadmin)


class ProductInBasketadmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInBasket._meta.fields]

    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketadmin)
