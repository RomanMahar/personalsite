# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-03 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180303_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagesection',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='home.CustomImage'),
        ),
    ]
