# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .companies import Company


class Currency(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Moneda')
    code = models.CharField(max_length=3, verbose_name='Identificador')
    symbol = models.CharField(max_length=3, verbose_name='Símbolo')

    def __unicode__(self):
        return '%s' % self.symbol

    class Meta:
        unique_together = ('company', 'code')
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'
        ordering = ['id']
