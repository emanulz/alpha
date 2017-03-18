# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.catalog import AccountViewSet, AccountLevelViewSet
from ..apis.entries import EntryViewSet, EntryDetailViewSet
from ..apis.reports import ReportViewSet

# from ..apis.clients import ClientViewSet

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'accountlevels', AccountLevelViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'entrydetails', EntryDetailViewSet)
router.register(r'reports', ReportViewSet)


urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
