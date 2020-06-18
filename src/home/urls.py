from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category=<slug:slug>/', views.index, name='index'),
    path('discount', views.discount_products, name='discount'),
    path('delivery', views.delivery, name='delivery'),
    path('info_shop', views.info_shop, name='info_shop')
]