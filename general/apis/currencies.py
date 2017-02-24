# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from ..models.currencies import Currency
from .filters.currencies import CurrencyFilter

# API


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'company', 'name', 'code', 'symbol',)


class CurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    lookup_field = 'id'
    filter_class = CurrencyFilter
