# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from ..models.products import Product
from general.models.companies import Company


class Recipe(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    product = models.OneToOneField(Product, verbose_name='Producto')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'
        ordering = ['id']


class RecipeDetail(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    recipe = models.ForeignKey('Recipe', verbose_name='Receta')
    product = models.ForeignKey(Product, null=True, verbose_name='Producto Bodega')
    qty = models.FloatField(null=True, default=1, verbose_name='Cantidad')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de receta'
        verbose_name_plural = 'Recetas - 1. Detalles de receta'
        ordering = ['id']
