# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-03-06 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_homepage_rel_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='rel_link',
        ),
    ]
