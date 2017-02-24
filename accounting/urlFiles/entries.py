# -*- coding: utf-8 -*-

from django.conf.urls import url
# from .views import product_list, ProductCreate, product_update, ProductDelete
from ..views.entries.create import entry_create
# from ..views.products.update import product_update
# from ..views.products.list import product_list

# from django.contrib.auth.decorators import login_required


urlpatterns = [

    url(r'^add/$', entry_create, name='entry_create'),
    # url(r'^add2/$', login_required(ProductCreate.as_view()), name='product_create'),
    # url(r'^delete/(?P<pk>[\w-]+)/$', login_required(ProductDelete.as_view()), name='product_delete'),
    # url(r'^(?P<pk>[\w-]+)/$', product_update, name='product_update'),
    # url(r'^$', product_list, name='product_list'),
    ]
