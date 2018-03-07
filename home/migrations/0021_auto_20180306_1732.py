# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-06 17:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_homepage_custommarkup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='main_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='homepagesection',
            name='orientation',
            field=models.CharField(choices=[('left', 'LEFT'), ('right', 'RIGHT'), ('centre', 'CENTRE'), ('freeform', 'FREEFORM')], default='left', max_length=50),
        ),
    ]
