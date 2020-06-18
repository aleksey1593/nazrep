from django.contrib import admin
from .models import *


class Buyeradmin(admin.ModelAdmin):
    list_display = [field.name for field in Buyer._meta.fields]
    list_filter = ["name",]
    search_fields = ["name"]

    class Meta:
        model = Buyer

admin.site.register(Buyer, Buyeradmin)
