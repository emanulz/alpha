# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.reports import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    def buttonGenerate(self, obj):
        return '<input id="%s" type="button" class="buttonGenerate" value="Generar">' % (obj.id)

    buttonGenerate.short_description = 'generar'
    buttonGenerate.allow_tags = True

    list_display = ('name', 'buttonGenerate', 'header', 'template')

    search_fields = ('name', 'header', 'template')

    class Media:
        css = {
            'all': ("../static/vendor/iziModal/css/iziModal.min.css",
                    "../static/myAdmin/accounting/reports/button.css", )
            }

        js = ("../static/myAdmin/accounting/reports/jquery.min.js",
              "../static/vendor/iziModal/js/iziModal.min.js",
              "../static/myAdmin/accounting/reports/button.js",
              )

    def save_model(self, request, obj, form, change):
        obj.company = request.user.profile.company
        super(ReportAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):

        qs = super(ReportAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(company=request.user.profile.company_id)
