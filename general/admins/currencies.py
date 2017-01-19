# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from ..models.currencies import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'symbol', )

    search_fields = ('id', 'name', 'symbol', )

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(CurrencyAdmin, self).save_model(request, obj, form, change)
