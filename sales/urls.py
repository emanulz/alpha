# -*- coding: utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [

    url(r'^products/', include('sales.urlFiles.products')),

    ]
