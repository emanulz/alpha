# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.currencies import Currency


class CurrencyFilter(django_filters.FilterSet):

    class Meta:
        model = Currency
        fields = ('id', 'company', 'name', 'code', 'symbol',)
