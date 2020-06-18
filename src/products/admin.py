from django.contrib import admin
from .models import *



class Categoryadmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category

admin.site.register(Category, Categoryadmin)


class Productadmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product

admin.site.register(Product, Productadmin)


class ProductImageadmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageadmin)
