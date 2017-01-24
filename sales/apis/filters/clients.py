# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.clients import Client


class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Client
        fields = ('id', 'company', 'name', 'last_name', 'code', 'id_type', 'id_num', 'contact', 'has_credit', 'debt',
                  'credit_limit', 'credit_days')
