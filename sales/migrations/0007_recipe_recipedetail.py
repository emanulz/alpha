# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0007_auto_20170118_1703'),
        ('sales', '0006_auto_20170119_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isComposed', models.BooleanField(default=True, verbose_name='Producto compuesto?')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sales.Product', verbose_name='Producto')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Receta',
                'verbose_name_plural': 'Recetas',
            },
        ),
        migrations.CreateModel(
            name='RecipeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField(default=1, null=True, verbose_name='Cantidad')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.Product', verbose_name='Producto Bodega')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Recipe', verbose_name='Receta')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Detalle de receta',
                'verbose_name_plural': 'Recetas - 1. Detalles de receta',
            },
        ),
    ]
