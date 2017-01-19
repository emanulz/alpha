# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from ..models.contacts import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'company', 'address', 'phone1', 'email1')

    search_fields = ('name', 'address', 'phone1', 'email1')

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ContactAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ContactAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)
