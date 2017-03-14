# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from ...models.catalog import Account, AccountLevel


# class AccountCategoryFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = AccountCategory
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'movements')
#
#
# class AccountGroupFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = AccountGroup
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'category', 'movements')


class AccountFilter(django_filters.FilterSet):

    class Meta:
        model = Account
        fields = ('id', 'company', 'name', 'identifier', 'nature', 'level', 'parent', 'active', 'movements')


class AccountLevelFilter(django_filters.FilterSet):

    class Meta:
        model = AccountLevel
        fields = ('id', 'company', 'name', 'level', 'identifierDigits')
#
#
# class SubAccountFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = SubAccount
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'account', 'movements')
#
#
# class DetailAccountFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = DetailAccount
#         fields = ('id', 'company', 'name', 'description', 'identifier', 'subaccount', 'movements')
