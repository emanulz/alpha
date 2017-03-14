# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.catalog import AccountViewSet, AccountLevelViewSet

# from ..apis.clients import ClientViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'accountlevels', AccountLevelViewSet)


urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
