# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-09 14:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20180209_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredientthings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.CharField(blank=True, help_text='Amount', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='ingredient_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='subrecipe',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipeprofile',
            name='amount',
            field=models.CharField(blank=True, help_text="Amount: e.g. '1 2/3 cups'", max_length=255),
        ),
        migrations.AlterField(
            model_name='recipeprofile',
            name='name_of_ingredient',
            field=models.CharField(help_text="Ingredient: e.g. 'Flour' ", max_length=255),
        ),
    ]
