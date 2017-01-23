# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from ..models.recipies import Recipe, RecipeDetail


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeDetail)
class RecipeDetailAdmin(admin.ModelAdmin):
    pass
