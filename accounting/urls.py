# -*- coding: utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [

    url(r'^entries/', include('accounting.urlFiles.entries')),
    url(r'^catalog/', include('accounting.urlFiles.catalog')),
    url(r'', include('accounting.urlFiles.api')),

    ]
