# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-20 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_recipe_recipedetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='isComposed',
        ),
    ]