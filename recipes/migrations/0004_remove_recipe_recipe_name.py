# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-09 03:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='recipe_name',
        ),
    ]
