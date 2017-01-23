# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models.companies import Company
from .catalog import Account, SubAccount, DetailAccount


class Entry(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    date = models.DateField(verbose_name='Fecha')
    detail = models.CharField(max_length=255, verbose_name='Detalle')
    totalDebit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Total Debe')
    totalCredit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Total Haber')
    difference = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Diferencia')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Asiento'
        verbose_name_plural = 'Asientos'
        ordering = ['id']


class EntryDetail(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    entry = models.ForeignKey('Entry', verbose_name='Asiento')
    account = models.ForeignKey(Account, verbose_name='Cuenta')
    subAccount = models.ForeignKey(SubAccount, verbose_name='Sub-Cuenta')
    detailAccount = models.ForeignKey(DetailAccount, verbose_name='Cuenta Detalle')
    debit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Debe')
    credit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Haber')

    def __unicode__(self):
        return 'Detalle de asiento %s' % self.entry.id

    class Meta:
        verbose_name = 'Detalle de Asiento'
        verbose_name_plural = 'Asientos - 1 .Detalles de Asiento'
        ordering = ['id']
