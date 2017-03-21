# -*- coding: utf-8 -*-

from django.conf.urls import include, url
from .views.reports.reports import report_create

urlpatterns = [

    url(r'^entries/', include('accounting.urlFiles.entries')),
    url(r'^catalog/', include('accounting.urlFiles.catalog')),
    url(r'reports/', report_create, name='report_create'),
    url(r'', include('accounting.urlFiles.api')),

    ]
