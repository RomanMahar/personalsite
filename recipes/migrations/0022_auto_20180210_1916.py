# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-10 19:16
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_recipeprofile_link_external'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeprofile',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='recipe_in_recipe', to='recipes.Recipe'),
        ),
    ]
