# -*- coding: utf-8 -*-

from django.conf.urls import include, url


from rest_framework import routers
from ..apis.products import ProductViewSet, ProductDepartmentViewSet, ProductSubDepartmentViewSet
from ..apis.clients import ClientViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'product_departments', ProductDepartmentViewSet)
router.register(r'product_subdepartments', ProductSubDepartmentViewSet)

router.register(r'clients', ClientViewSet)

urlpatterns = [

    url(r'^api/', include(router.urls)),
    ]
