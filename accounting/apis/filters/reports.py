# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.reports import Report


class ReportFilter(django_filters.FilterSet):

    class Meta:
        model = Report
        fields = ('id', 'company', 'name', 'header', 'accountsToSum', 'accountsToShow', 'template')
