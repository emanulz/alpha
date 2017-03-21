# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from general.models.companies import Company
from django.core.validators import RegexValidator, MaxValueValidator


class Catalog(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Catálogo'
        verbose_name_plural = 'Catálogo'
        ordering = ['id']


class Account(models.Model):

    deb = 'deb'
    hab = 'hab'

    NATURE_CHOICES = ((deb, 'Debe'),
                      (hab, 'Haber'),
                      )

    company = models.ForeignKey(Company, verbose_name='Empresa')
    name = models.CharField(max_length=255, verbose_name='Nombre')
    identifier = models.CharField(max_length=3, verbose_name='Identificador')
    nature = models.CharField(max_length=3, choices=NATURE_CHOICES, default=deb, verbose_name='Naturaleza')
    level = models.ForeignKey('AccountLevel', verbose_name='Nivel de la Cuenta')
    parent = models.ForeignKey('self', blank=True, null=True, verbose_name='Cuenta Padre')
    movements = models.BooleanField(default=False, verbose_name='Acepta Movimiento?')
    active = models.BooleanField(default=True, verbose_name='Cuenta Activa?')

    def __unicode__(self):
        return '%s %s' % (self.identifier, self.name)

    class Meta:
        verbose_name = 'Cuenta Contable'
        verbose_name_plural = 'Catálogo - 1. Cuentas Contables'
        ordering = ['id']

    @property
    def level_num(self):
        return self.level.level


class AccountLevel(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    level = models.PositiveIntegerField(verbose_name='Nivel de cuenta')
    identifierDigits = models.PositiveIntegerField(default=1, verbose_name='Digitos de indentificador')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        unique_together = ('company', 'level')
        verbose_name = 'Nivel de Cuenta'
        verbose_name_plural = 'Catálogo - 2. Niveles de Cuenta'
        ordering = ['id']



#
# class AccountCategory(models.Model):
#
#     deb = 'deb'
#     hab = 'hab'
#
#     NATURE_CHOICES = ((deb, 'Debe'),
#                       (hab, 'Haber'),
#                       )
#
#     company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
#     name = models.CharField(max_length=255, verbose_name='Nombre')
#     description = models.CharField(max_length=255, verbose_name='Descripción')
#     identifier = models.CharField(max_length=1, verbose_name='Identificador')
#     nature = models.CharField(max_length=3, choices=NATURE_CHOICES, default=deb, verbose_name='Naturaleza')
#     movements = models.BooleanField(default=False, verbose_name='Acepta Movimiento?')
#
#     def __unicode__(self):
#         return '%s' % self.name
#
#     class Meta:
#         verbose_name = 'Tipo de Cuenta'
#         verbose_name_plural = 'Catálogo - 1. Tipos de Cuentas'
#         ordering = ['id']
#
#

# class SubAccount(models.Model):
#
#     company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
#     name = models.CharField(max_length=255, verbose_name='Nombre')
#     description = models.CharField(max_length=255, verbose_name='Descripción')
#     identifier = models.CharField(max_length=3, verbose_name='Identificador de subcuenta',
#                                   validators=[RegexValidator(regex='^.{2}$',
#                                               message='El identificador debe ser de dos dígitos',
#                                               code='nomatch')])
#     account = models.ForeignKey('Account', verbose_name='Cuenta Mayor')
#     movements = models.BooleanField(default=False, verbose_name='Acepta Movimiento?')
#
#     def __unicode__(self):
#         return '%s-%s %s' % (self.account.identifier, self.identifier, self.name)
#
#     class Meta:
#         verbose_name = 'Sub-Cuenta'
#         verbose_name_plural = 'Catálogo - 4. Sub-Cuentas'
#         ordering = ['id']
#
#
# class DetailAccount(models.Model):
#
#     company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
#     name = models.CharField(max_length=255, verbose_name='Nombre')
#     description = models.CharField(max_length=255, verbose_name='Descripción')
#     identifier = models.CharField(max_length=2, verbose_name='Identificador de subcuenta',
#                                   validators=[RegexValidator(regex='^.{2}$',
#                                               message='El identificador debe ser de dos dígitos',
#                                               code='nomatch')])
#     subaccount = models.ForeignKey('SubAccount', verbose_name='Sub-Cuenta')
#     movements = models.BooleanField(default=False, verbose_name='Acepta Movimiento?')
#
#     def __unicode__(self):
#         return '%s-%s-%s %s' % (self.subaccount.account.identifier, self.subaccount.identifier, self.identifier,
#                                 self.name)
#
#     class Meta:
#         verbose_name = 'Cuenta Detalle'
#         verbose_name_plural = 'Catálogo - 5. Cuentas Detalle'
#         ordering = ['id']
