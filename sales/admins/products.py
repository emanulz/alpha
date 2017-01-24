# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.admin.views.main import ChangeList
from ..models.products import Product, ProductDepartment, ProductSubDepartment


class ProductChangeList(ChangeList):
    def url_for_result(self, result):
        code = result.code
        return '/sales/products/%d/' % (code)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum', 'unit',
                    'cost', 'isactive', 'hasforsale')

    search_fields = ('code', 'description', 'department__name', 'subdepartment__name', 'useinventory', 'minimum', 'unit',
                     'cost', 'isactive', 'hasforsale')

    def get_changelist(self, request, **kwargs):
        return ProductChangeList

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ProductAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ProductAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(company=request.user.profile.company_id)


# @admin.register(ProductForSale)
# class ProductForSaleAdmin(admin.ModelAdmin):
#
#     list_display = ('id', 'code', 'company', 'product', 'barcode', 'description', 'department', 'subdepartment',
#                     'utility', 'price', 'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)
#
#     search_fields = ('id', 'code', 'company', 'product__description', 'barcode', 'description', 'department',
#                      'subdepartment', 'utility', 'price', 'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(ProductForSaleAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(ProductForSaleAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             # It is mine, all mine. Just return everything.
#             return qs
#         # Now we just add an extra filter on the queryset and
#         # we're done. Assumption: Page.owner is a foreignkey
#         # to a User.
#         return qs.filter(company=request.user.profile.company_id)


@admin.register(ProductDepartment)
class ProductDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'code',)
    search_fields = ('id', 'name', 'code',)

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ProductDepartmentAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ProductDepartmentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(company=request.user.profile.company_id)


@admin.register(ProductSubDepartment)
class ProductSubDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'department', 'code', )
    search_fields = ('id', 'name', 'department', 'code', )

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ProductSubDepartmentAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ProductSubDepartmentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset and
        # we're done. Assumption: Page.owner is a foreignkey
        # to a User.
        return qs.filter(company=request.user.profile.company_id)
