# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Recipe, RecipeDetail


class RecipeFilter(django_filters.FilterSet):

    class Meta:
        model = Recipe
        fields = ('id', 'product', 'isComposed')


class RecipeDetailFilter(django_filters.FilterSet):

    class Meta:
        model = RecipeDetail
        fields = ('id', 'product', 'qty', 'recipe')
