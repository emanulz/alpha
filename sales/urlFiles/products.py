# -*- coding: utf-8 -*-

from django.conf.urls import include, url
# from .views import product_list, ProductCreate, product_update, ProductDelete
from ..views.products.create import product_create
from ..views.products.update import product_update
from ..views.products.list import product_list

# from django.contrib.auth.decorators import login_required

from rest_framework import routers
from ..apis.products import ProductViewSet, ProductDepartmentViewSet, ProductSubDepartmentViewSet, ProductForSaleViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'productsforsale', ProductForSaleViewSet)
router.register(r'product_departments', ProductDepartmentViewSet)
router.register(r'product_subdepartments', ProductSubDepartmentViewSet)

urlpatterns = [

    url(r'^add/$', product_create, name='product_create'),
    url(r'^api/', include(router.urls)),
    # url(r'^add2/$', login_required(ProductCreate.as_view()), name='product_create'),
    # url(r'^delete/(?P<pk>[\w-]+)/$', login_required(ProductDelete.as_view()), name='product_delete'),
    url(r'^(?P<pk>[\w-]+)/$', product_update, name='product_update'),
    url(r'^$', product_list, name='product_list'),
    ]
