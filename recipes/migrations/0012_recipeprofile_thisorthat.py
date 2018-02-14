# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-10 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20180209_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeprofile',
            name='thisOrThat',
            field=models.BooleanField(default=False, help_text="Adds 'Or' between this and next ingredient"),
        ),
    ]
