# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.currencies import CurrencyViewSet


router = routers.DefaultRouter()
router.register(r'currencies', CurrencyViewSet)


urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
