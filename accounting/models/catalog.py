# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models.companies import Company


class AccountCategory(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    identifier = models.CharField(max_length=2, verbose_name='Identificador')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Tipo de Cuenta'
        verbose_name_plural = 'Catálogo - 1 .Tipos de Cuentas'
        ordering = ['id']


class Account(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    identifier = models.CharField(max_length=3, verbose_name='Identificador de subcuenta')
    category = models.ForeignKey('AccountCategory', verbose_name='Tipo de Cuenta')

    def __unicode__(self):
        return '%s %s' % (self.identifier, self.name)

    class Meta:
        verbose_name = 'Cuenta Mayor'
        verbose_name_plural = 'Catálogo - 2 .Cuentas Mayores'
        ordering = ['id']


class SubAccount(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    identifier = models.CharField(max_length=3, verbose_name='Identificador de subcuenta')
    account = models.ForeignKey('Account', verbose_name='Cuenta Mayor')

    def __unicode__(self):
        return '%s-%s %s' % (self.account.identifier, self.identifier, self.name)

    class Meta:
        verbose_name = 'Sub-Cuenta'
        verbose_name_plural = 'Catálogo - 3 .Sub-Cuentas'
        ordering = ['id']


class DetailAccount(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    identifier = models.CharField(max_length=3, verbose_name='Identificador de Detalle')
    subaccount = models.ForeignKey('SubAccount', verbose_name='Sub-Cuenta')

    def __unicode__(self):
        return '%s-%s-%s %s' % (self.subaccount.account.identifier, self.subaccount.identifier, self.identifier,
                                self.name)

    class Meta:
        verbose_name = 'Cuenta Detalle'
        verbose_name_plural = 'Catálogo - 4 Cuentas Detalle'
        ordering = ['id']
