# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets, filters
from ..models.catalog import Account, AccountLevel
from .filters.catalog import AccountFilter, AccountLevelFilter


# API

class AccountLevelSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccountLevel
        fields = ('id', 'company', 'name', 'level', 'identifierDigits')


class AccountLevelViewSet(viewsets.ModelViewSet):

    serializer_class = AccountLevelSerializer
    queryset = AccountLevel.objects.all()
    lookup_field = 'id'
    filter_class = AccountLevelFilter
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'level')
    ordering = ('level',)


# API

class AccountSerializer(serializers.ModelSerializer):

    level_num = serializers.ReadOnlyField()

    class Meta:
        model = Account
        fields = ('id', 'company', 'name', 'identifier', 'nature', 'level', 'level_num', 'parent', 'active', 'movements')


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'id'
    filter_class = AccountFilter
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'identifier')
    ordering = ('identifier',)
# class AccountCategorySerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = AccountCategory
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'movements')
#
#
# class AccountCategoryViewSet(viewsets.ModelViewSet):
#
#     serializer_class = AccountCategorySerializer
#     queryset = AccountCategory.objects.all()
#     lookup_field = 'id'
#     filter_class = AccountCategoryFilter

# # ----------------------------------------------------------------------------
#
#
# class AccountGroupSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = AccountGroup
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'category', 'movements')
#
#
# class AccountGroupViewSet(viewsets.ModelViewSet):
#
#     serializer_class = AccountGroupSerializer
#     queryset = AccountGroup.objects.all()
#     lookup_field = 'id'
#     filter_class = AccountGroupFilter
#
# # ----------------------------------------------------------------------------



# # ----------------------------------------------------------------------------
#
#
# class SubAccountSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = SubAccount
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'account', 'movements')
#
#
# class SubAccountViewSet(viewsets.ModelViewSet):
#
#     serializer_class = SubAccountSerializer
#     queryset = SubAccount.objects.all()
#     lookup_field = 'id'
#     filter_class = SubAccountFilter
#
# # ----------------------------------------------------------------------------
#
#
# class DetailAccountSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = DetailAccount
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'subaccount', 'movements')
#
#
# class DetailAccountViewSet(viewsets.ModelViewSet):
#
#     serializer_class = DetailAccountSerializer
#     queryset = DetailAccount.objects.all()
#     lookup_field = 'id'
#     filter_class = DetailAccountFilter

# ----------------------------------------------------------------------------
