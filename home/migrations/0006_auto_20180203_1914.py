# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-02-03 19:14
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepagesection_streambody'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagesection',
            name='streamBody',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full-title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('markup', wagtail.wagtailcore.blocks.RawHTMLBlock())], blank=True, null=True),
        ),
    ]
