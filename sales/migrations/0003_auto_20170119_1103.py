# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 17:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20170119_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Descuento %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sellprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Precio de Venta \u20a1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='taxes',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4, null=True, verbose_name='Impuestos %'),
        ),
        migrations.AlterField(
            model_name='product',
            name='utility',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True, verbose_name='Utilidad %'),
        ),
    ]
