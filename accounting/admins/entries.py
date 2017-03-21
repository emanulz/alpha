# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.entries import Entry, EntryDetail


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    list_display = ('id', 'date', 'entryDate', 'totalDebe', 'totalHaber', 'difference')

    search_fields = ('id', 'date', 'entryDate', 'totalDebe', 'totalHaber', 'difference')

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

    list_display = ('id', 'date', 'entry', 'account', 'debe', 'haber')

    search_fields = ('id', 'date', 'entry', 'account', 'debe', 'haber')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(EntryDetailAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(EntryDetailAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)
