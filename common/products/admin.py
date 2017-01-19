# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from.models import Product, ProductDepartment, ProductSubDepartment, ProductForSale


class ProductChangeList(ChangeList):
    def url_for_result(self, result):
        code = result.code
        return '/products/%d/' % (code)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum', 'unit',
                    'cost', 'isactive', 'hasforsale')

    search_fields = ('id', 'code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum', 'unit',
                     'cost', 'isactive', 'hasforsale')

    def get_changelist(self, request, **kwargs):
        return ProductChangeList

    def get_queryset(self, request):

        qs = super(ProductAdmin, self).get_queryset(request)
        # if request.user.is_superuser:
        #     # It is mine, all mine. Just return everything.
        #     return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(company=request.user.profile.company_id)


@admin.register(ProductForSale)
class ProductForSaleAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'company', 'product', 'barcode', 'description', 'department', 'subdepartment', 'utility', 'price',
                   'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)

    search_fields = ('id', 'code', 'company', 'product__description', 'barcode', 'description', 'department', 'subdepartment', 'utility', 'price',
                     'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)


@admin.register(ProductDepartment)
class ProductDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'code',)
    search_fields = ('id', 'name', 'code',)


@admin.register(ProductSubDepartment)
class ProductSubDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'department', 'code', )
    search_fields = ('id', 'name', 'department', 'code', )
