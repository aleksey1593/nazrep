from django.urls import path

from . import views

urlpatterns = [

    path(r'^search/$', views.search, name='search'),

]
