# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-13 01:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0028_recipe_featured_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='subrecipe',
        ),
    ]
