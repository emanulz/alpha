# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from general.models.companies import Company
from general.models.contacts import Contact


class Client(models.Model):

    person = 'per'
    juridic = 'jur'
    passport = 'pas'

    ID_TYPE_CHOICES = ((person, 'Cédula Física'),
                       (juridic, 'Cédula Jurídica'),
                       (passport, 'Pasaporte'),
                       )

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Apellidos')
    code = models.CharField(max_length=10, null=True, verbose_name='Código')
    id_type = models.CharField(max_length=3, choices=ID_TYPE_CHOICES, default=person,
                               verbose_name='Tipo de Identificación')
    id_num = models.CharField(max_length=255, null=True, blank=True, verbose_name='Num Identificación')
    contact = models.ForeignKey(Contact, verbose_name='Contacto')
    has_credit = models.BooleanField(default=False, verbose_name='Tiene Crédito?')
    credit_limit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Límite de Crédito', null=True,
                                       blank=True, default=0)
    debt = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Saldo', null=True, blank=True, default=0)
    credit_days = models.PositiveIntegerField(default=30, null=True, blank=True, verbose_name='Días de Crédito')

    def __unicode__(self):
        return '%s %s' % (self.name, self.last_name)

    class Meta:
        unique_together = (('company', 'id_num'), ('company', 'code'))
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']
