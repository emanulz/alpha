# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from ..models.clients import Client
from general.models.companies import Company


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = ('code', 'name', 'last_name', 'id_type', 'id_num', 'has_credit', 'credit_limit',
                    'debt', 'credit_days', )

    search_fields = ('name', 'code', 'last_name', 'id_type', 'id_num', 'has_credit', 'credit_limit',
                     'debt', 'credit_days', )

    # def render_change_form(self, request, context, *args, **kwargs):
    #     context['adminform'].form.fields['company'].queryset = Company.objects.filter(id=request.user.profile.company.id)
    #     return super(ClientAdmin, self).render_change_form(request, context, args, kwargs)

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ClientAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ClientAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)
