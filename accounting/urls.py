# -*- coding: utf-8 -*-

from django.conf.urls import include, url

urlpatterns = [

    url(r'^entries/', include('accounting.urlFiles.entries')),
    url(r'', include('accounting.urlFiles.api')),

    ]
