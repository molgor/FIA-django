# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-23 21:17
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoFIA', '0006_auto_20170821_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treesperyear',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(db_index=True, geography=True, srid=4326),
        ),
    ]
