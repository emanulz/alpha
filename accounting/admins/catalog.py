# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.catalog import Account, AccountLevel


# @admin.register(Catalog)
# class CatalogAdmin(admin.ModelAdmin):
#
#     list_display = ('name',)
#
#     search_fields = ('name',)
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(AccountAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(CatalogAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(company=request.user.profile.company_id)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):

    list_display = ('identifier', 'name', 'movements')

    search_fields = ('identifier', 'name')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(AccountAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(AccountAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)


@admin.register(AccountLevel)
class AccountLevelAdmin(admin.ModelAdmin):

    list_display = ('name', 'level')

    search_fields = ('name', 'level')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(AccountLevelAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(AccountLevelAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)

# @admin.register(AccountCategory)
# class AccountCategoryAdmin(admin.ModelAdmin):
#
#     list_display = ('identifier', 'name', 'description', 'movements')
#
#     search_fields = ('identifier', 'name', 'description')
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(AccountCategoryAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(AccountCategoryAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(company=request.user.profile.company_id)
#
#
# @admin.register(AccountGroup)
# class AccountGroupAdmin(admin.ModelAdmin):
#
#     list_display = ('identifier', 'name', 'description', 'movements')
#
#     search_fields = ('identifier', 'name', 'description')
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(AccountGroupAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(AccountGroupAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(company=request.user.profile.company_id)
#
#
# @admin.register(SubAccount)
# class SubAccountAdmin(admin.ModelAdmin):
#
#     list_display = ('identifier', 'name', 'description', 'account', 'movements')
#
#     search_fields = ('identifier', 'name', 'description', 'account__name')
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(SubAccountAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(SubAccountAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(company=request.user.profile.company_id)
#
#
# @admin.register(DetailAccount)
# class DetailAccountAdmin(admin.ModelAdmin):
#
#     list_display = ('identifier', 'name', 'description', 'subaccount', 'movements')
#
#     search_fields = ('identifier', 'name', 'description', 'subaccount__name', 'subaccount__account')
#
#     def save_model(self, request, obj, form, change):
#         obj.company = request.user.profile.company
#         super(DetailAccountAdmin, self).save_model(request, obj, form, change)
#
#     def get_queryset(self, request):
#
#         qs = super(DetailAccountAdmin, self).get_queryset(request)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(company=request.user.profile.company_id)
