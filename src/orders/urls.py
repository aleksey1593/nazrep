from django.urls import path

from . import views

urlpatterns = [
    path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    path(r'checkout/$', views.checkout, name='checkout'),
    path('checkout/thanks/', views.checkout_thanks, name='checkout_thanks'),
]