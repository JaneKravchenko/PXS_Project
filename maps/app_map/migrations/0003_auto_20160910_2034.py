# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 20:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_map', '0002_auto_20160910_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worldborderl',
            name='area',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='fips',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='iso2',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='iso3',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='mpoly',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='pop2005',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='region',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='subregion',
        ),
        migrations.RemoveField(
            model_name='worldborderl',
            name='un',
        ),
    ]
