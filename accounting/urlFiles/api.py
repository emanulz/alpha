# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.catalog import AccountViewSet

# from ..apis.clients import ClientViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
