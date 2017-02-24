# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.catalog import AccountCategoryViewSet, AccountViewSet, SubAccountViewSet, DetailAccountViewSet
from ..apis.catalog import AccountGroupViewSet
# from ..apis.clients import ClientViewSet

router = routers.DefaultRouter()
router.register(r'account_categories', AccountCategoryViewSet)
router.register(r'account_groups', AccountGroupViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'subaccounts', SubAccountViewSet)
router.register(r'detailaccounts', DetailAccountViewSet)

urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
