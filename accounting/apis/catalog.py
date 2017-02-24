# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets, filters
from ..models.catalog import AccountCategory, Account, SubAccount, DetailAccount, AccountGroup
from .filters.catalog import AccountCategoryFilter, AccountFilter, SubAccountFilter, DetailAccountFilter
from .filters.catalog import AccountGroupFilter

# API


class AccountCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountCategory
        fields = ('id', 'company', 'name', 'description', 'identifier', 'movements')


class AccountCategoryViewSet(viewsets.ModelViewSet):

    serializer_class = AccountCategorySerializer
    queryset = AccountCategory.objects.all()
    lookup_field = 'id'
    filter_class = AccountCategoryFilter

# ----------------------------------------------------------------------------


class AccountGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountGroup
        fields = ('id', 'company', 'name', 'description', 'identifier', 'category', 'movements')


class AccountGroupViewSet(viewsets.ModelViewSet):

    serializer_class = AccountGroupSerializer
    queryset = AccountGroup.objects.all()
    lookup_field = 'id'
    filter_class = AccountGroupFilter

# ----------------------------------------------------------------------------


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'company', 'name', 'description', 'identifier', 'group', 'movements')


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'id'
    filter_class = AccountFilter
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'identifier')
    ordering = ('identifier',)

# ----------------------------------------------------------------------------


class SubAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubAccount
        fields = ('id', 'company', 'name', 'description', 'identifier', 'account', 'movements')


class SubAccountViewSet(viewsets.ModelViewSet):

    serializer_class = SubAccountSerializer
    queryset = SubAccount.objects.all()
    lookup_field = 'id'
    filter_class = SubAccountFilter

# ----------------------------------------------------------------------------


class DetailAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = DetailAccount
        fields = ('id', 'company', 'name', 'description', 'identifier', 'subaccount', 'movements')


class DetailAccountViewSet(viewsets.ModelViewSet):

    serializer_class = DetailAccountSerializer
    queryset = DetailAccount.objects.all()
    lookup_field = 'id'
    filter_class = DetailAccountFilter

# ----------------------------------------------------------------------------
