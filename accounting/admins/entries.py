# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.entries import Entry, EntryDetail


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    list_display = ('id', 'date', 'entyDate', 'totalDebit', 'totalCredit', 'difference')

    search_fields = ('id', 'date', 'entyDate', 'totalDebit', 'totalCredit', 'difference')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(EntryAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(EntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)


@admin.register(EntryDetail)
class EntryDetailAdmin(admin.ModelAdmin):

    list_display = ('id', 'entry', 'account', 'subAccount', 'detailAccount', 'debit', 'credit')

    search_fields = ('id', 'entry', 'account', 'subAccount', 'detailAccount', 'debit', 'credit')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(EntryDetailAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(EntryDetailAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)
