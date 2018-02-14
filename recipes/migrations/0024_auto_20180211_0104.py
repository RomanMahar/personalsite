# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-11 01:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_auto_20180210_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='subrecipe',
        ),
        migrations.AddField(
            model_name='recipe',
            name='subrecipe',
            field=models.ManyToManyField(blank=True, help_text='Links to another recipe page.', null=True, to='recipes.Recipe'),
        ),
    ]
