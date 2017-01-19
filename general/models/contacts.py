# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from .companies import Company


class Contact(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa', editable=False)
    name = models.CharField(max_length=255, verbose_name='Nombre')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Dirección')
    phone1 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono principal')
    phone2 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono 2')
    phone3 = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono 3')
    email1 = models.EmailField(null=True, blank=True, verbose_name='Email principal')
    email2 = models.EmailField(null=True, blank=True, verbose_name='Email 2')
    email3 = models.EmailField(null=True, blank=True, verbose_name='Email 3')

    def __unicode__(self):
        return '%s' % (self.name)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = ' Contactos'
        ordering = ['id']
