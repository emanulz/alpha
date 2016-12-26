# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Recipe, RecipeDetail


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ('id', 'product', 'isComposed')

    search_fields = ('id', 'product', 'isComposed')


@admin.register(RecipeDetail)
class RecipeDetailAdmin(admin.ModelAdmin):

    list_display = ('id', 'product', 'qty', 'recipe')

    search_fields = ('id', 'product', 'qty', 'recipe__id')
