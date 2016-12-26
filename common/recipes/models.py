# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from common.products.models import Product


class Recipe(models.Model):

    product = models.OneToOneField(Product, verbose_name='Producto')
    isComposed = models.BooleanField(default=True, verbose_name='Producto compuesto?')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['id']


class RecipeDetail(models.Model):

    product = models.ForeignKey(Product, null=True, verbose_name='Producto Bodega')
    qty = models.FloatField(null=True, default=1, verbose_name='Cantidad')
    recipe = models.ForeignKey('Recipe', verbose_name='Receta')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de receta'
        verbose_name_plural = 'Detalles de receta'
        ordering = ['id']

# class Recipe2(models.Model):
#
#     productForSale = models.OneToOneField(ProductForSale, null=True, verbose_name='Producto de Venta')
#     recipes = models.ManyToManyField('self', blank=True, symmetrical=False, through='RecipeDetail')
#
#     def __unicode__(self):
#         return '%s' % self.id
#
#     class Meta:
#         verbose_name = 'Receta'
#         verbose_name_plural = 'Recetas'
#         ordering = ['id']
#
#
# class RecipeDetail2(models.Model):
#
#     from_recipe = models.ForeignKey('Recipe', related_name='from_recipe')
#     to_recipe = models.ForeignKey('Recipe', related_name='to_recipe')
#     qty = models.FloatField(verbose_name='Cantidad')
#
#     def __unicode__(self):
#         return '%s' % self.id
#
#     class Meta:
#         unique_together = ('from_recipe', 'to_recipe')
#         verbose_name = 'Detalle de Receta'
#         verbose_name_plural = 'Detalles de Receta'
#         ordering = ['id']
#
#
#   class SubRecipe2(models.Model):
#
#     recipe = models.ForeignKey('Recipe', verbose_name='Receta')
#     product = models.ForeignKey(Product, null=True, verbose_name='Producto Bodega')
#     qty = models.FloatField(null=True, default=1, verbose_name='Cantidad')
#
#    def __unicode__(self):
#         return '%s' % self.id
#
#     class Meta:
#         verbose_name = 'Sub-Receta'
#         verbose_name_plural = 'Sub-Recetas'
#         ordering = ['id']
