# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-19 16:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('general', '0007_auto_20170118_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Apellidos')),
                ('code', models.CharField(max_length=10, null=True, verbose_name='C\xf3digo')),
                ('id_type', models.CharField(choices=[('per', 'C\xe9dula F\xedsica'), ('jur', 'C\xe9dula Jur\xeddica'), ('pas', 'Pasaporte')], default='per', max_length=3, verbose_name='Tipo de Identificaci\xf3n')),
                ('id_num', models.CharField(blank=True, max_length=255, null=True, verbose_name='Num Identificaci\xf3n')),
                ('has_credit', models.BooleanField(default=False, verbose_name='Tiene Cr\xe9dito?')),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='L\xedmite de Cr\xe9dito')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=11, null=True, verbose_name='Saldo')),
                ('credit_days', models.PositiveIntegerField(blank=True, default=30, null=True, verbose_name='D\xedas de Cr\xe9dito')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.Contact', verbose_name='Contacto')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.PositiveIntegerField(default=0, verbose_name='C\xf3digo')),
                ('barcode', models.PositiveIntegerField(blank=True, default=0, verbose_name='C\xf3digo de Barras')),
                ('description', models.CharField(max_length=255, null=True, verbose_name='Descripci\xf3n del producto')),
                ('useinventory', models.BooleanField(default=False, verbose_name='Sistema de Inventarios?')),
                ('minimum', models.FloatField(default=0, verbose_name='M\xednimo en inventario')),
                ('unit', models.CharField(max_length=4, null=True, verbose_name='Unidad')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo \u20a1')),
                ('hasforsale', models.BooleanField(default=False, verbose_name='Es para Venta?')),
                ('utility', models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Utilidad %')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio sin Impuestos \u20a1')),
                ('usetaxes', models.BooleanField(default=False, verbose_name='Usa Impuestos?')),
                ('taxes', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Impuestos %')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=4, verbose_name='Descuento %')),
                ('sellprice', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio de Venta \u20a1')),
                ('isactive', models.BooleanField(default=True, verbose_name='Activo?')),
                ('iscomposed', models.BooleanField(default=False, verbose_name='Es Compuesto?')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='ProductDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la Familia')),
                ('code', models.CharField(max_length=2, verbose_name='Identificador de Familia')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Familia',
                'verbose_name_plural': 'Productos - 1. Familias',
            },
        ),
        migrations.CreateModel(
            name='ProductSubDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nombre de la Sub-Familia')),
                ('code', models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')),
                ('company', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='general.Company', verbose_name='Empresa')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.ProductDepartment', verbose_name='Familia')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Sub-Familia',
                'verbose_name_plural': 'Productos - 2. Sub-Familias',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='department',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.ProductDepartment', verbose_name='Familia'),
        ),
        migrations.AddField(
            model_name='product',
            name='subdepartment',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sales.ProductSubDepartment', verbose_name='Sub-Familia'),
        ),
        migrations.AlterUniqueTogether(
            name='productsubdepartment',
            unique_together=set([('department', 'code'), ('department', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='productdepartment',
            unique_together=set([('company', 'name'), ('company', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('company', 'barcode'), ('company', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set([('company', 'code'), ('company', 'id_num')]),
        ),
    ]
