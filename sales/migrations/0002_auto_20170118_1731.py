# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-18 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_auto_20170118_1703'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsubdepartment',
            name='company',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productdepartment',
            name='company',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productforsale',
            name='company',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa'),
            preserve_default=False,
        ),
    ]
