# -*- coding: utf-8 -*-
from django.conf.urls import url
# from .views import product_list, ProductCreate, product_update, ProductDelete
from .views.create import create
from .views.update import update
from .views.list import list
# from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^add/$', create, name='create'),
    # url(r'^add2/$', login_required(ProductCreate.as_view()), name='product_create'),
    # url(r'^delete/(?P<pk>[\w-]+)/$', login_required(ProductDelete.as_view()), name='product_delete'),
    url(r'^(?P<pk>[\w-]+)/$', update, name='update'),
    url(r'^$', list, name='list'),
    ]
