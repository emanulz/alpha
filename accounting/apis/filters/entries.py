# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.entries import Entry, EntryDetail


class EntryFilter(django_filters.FilterSet):

    class Meta:
        model = Entry
        fields = ('id', 'company', 'date', 'entryDate', 'totalDebe', 'totalHaber', 'difference')


class EntryDetailFilter(django_filters.FilterSet):

    class Meta:
        model = EntryDetail
        fields = ('id', 'company', 'entry', 'date', 'account', 'debe', 'haber', 'detail', 'document',)
