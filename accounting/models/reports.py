# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models.companies import Company
from accounting.models.catalog import Account


class Report(models.Model):

    tmp1 = 'tmp1'
    tmp2 = 'tmp2'
    tmp3 = 'tmp3'
    tmp4 = 'tmp4'

    TEMPLATE_CHOICES = ((tmp1, 'Asiento de Diario'),
                        (tmp2, 'Balance General'),
                        (tmp3, 'Estado de Resultados'),
                        (tmp2, 'Pérdidas y Ganancias'),
                        )

    company = models.ForeignKey(Company, verbose_name='Empresa')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    header = models.CharField(max_length=255, verbose_name='Encabezado')
    accountsToSum = models.ManyToManyField(Account, verbose_name='Cuentas a sumar', related_name='Sum')
    accountsToShow = models.ManyToManyField(Account, verbose_name='Cuentas a mostrar', related_name='Show')
    template = models.CharField(max_length=4, verbose_name='Plantilla', choices=TEMPLATE_CHOICES)

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['id']
