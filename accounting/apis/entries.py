# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from ..models.entries import Entry, EntryDetail
from .filters.entries import EntryFilter, EntryDetailFilter

# API


class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('id', 'company', 'date', 'entryDate', 'totalDebe', 'totalHaber', 'difference')


class EntryViewSet(viewsets.ModelViewSet):

    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    lookup_field = 'id'
    filter_class = EntryFilter


# API

class EntryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryDetail
        fields = ('id', 'company', 'entry', 'date', 'account', 'debe', 'haber', 'detail', 'document',)


class EntryDetailViewSet(viewsets.ModelViewSet):

    serializer_class = EntryDetailSerializer
    queryset = EntryDetail.objects.all()
    lookup_field = 'id'
    filter_class = EntryDetailFilter
