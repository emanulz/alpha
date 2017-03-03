# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models.companies import Company


class Expense(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    date = models.DateField(verbose_name='Fecha')
    billDate = models.DateField(verbose_name='Fecha de Factura', null=True, blank=True)
    description = models.CharField(max_length=255, verbose_name='Detalle')
    document = models.CharField(max_length=255, verbose_name='Documento')
    total = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Precio Total')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['id']
