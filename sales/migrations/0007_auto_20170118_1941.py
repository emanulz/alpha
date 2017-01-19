# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 01:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_auto_20170118_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa'),
        ),
    ]
