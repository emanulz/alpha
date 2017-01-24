# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.products import Product, ProductDepartment, ProductSubDepartment


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ('id', 'company', 'code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum',
                  'unit', 'cost', 'utility', 'usetaxes', 'price', 'taxes', 'discount', 'sellprice', 'isactive',
                  'hasforsale')


# class ProductForSaleFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = ProductForSale
#         fields = ('id', 'code', 'company', 'product', 'barcode', 'description', 'department', 'subdepartment',
#                   'utility', 'price', 'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)


class ProductDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductDepartment
        fields = ('id', 'name', 'code',)


class ProductSubDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductSubDepartment
        fields = ('id', 'name', 'department', 'code', )
