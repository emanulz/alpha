# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Recipe, RecipeDetail
from .filters import RecipeFilter, RecipeDetailFilter


# API

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'product', 'isComposed')


class RecipeViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    lookup_field = 'id'
    filter_class = RecipeFilter


class RecipeDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecipeDetail
        fields = ('id', 'product', 'qty', 'recipe')


class RecipeDetailViewSet(viewsets.ModelViewSet):

    serializer_class = RecipeDetailSerializer
    queryset = RecipeDetail.objects.all()
    lookup_field = 'id'
    filter_class = RecipeDetailFilter
