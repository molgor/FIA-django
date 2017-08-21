# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-21 14:04
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Richness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateab', models.CharField(db_index=True, max_length=254)),
                ('statenm', models.CharField(db_index=True, max_length=254)),
                ('countynm', models.CharField(db_index=True, max_length=254)),
                ('plot_idn', models.BigIntegerField(db_index=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('elev', models.FloatField(db_index=True)),
                ('invyr', models.BigIntegerField()),
                ('area', models.BigIntegerField()),
                ('s', models.BigIntegerField()),
                ('tree_dens', models.BigIntegerField()),
                ('plot_agb', models.FloatField(db_index=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(db_index=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Spplist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stateab', models.CharField(db_index=True, max_length=254)),
                ('statenm', models.CharField(db_index=True, max_length=254)),
                ('countynm', models.CharField(db_index=True, max_length=254)),
                ('plot_idn', models.FloatField(db_index=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('elev', models.FloatField(db_index=True)),
                ('spcd', models.BigIntegerField()),
                ('genus', models.CharField(db_index=True, max_length=254)),
                ('species', models.CharField(db_index=True, max_length=254)),
                ('variety', models.CharField(db_index=True, max_length=254)),
                ('subspecies', models.CharField(db_index=True, max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.PointField(db_index=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='TreeLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('study', models.CharField(db_index=True, max_length=254)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('plot_id', models.BigIntegerField(db_index=True)),
                ('plotarea_m', models.BigIntegerField()),
                ('year', models.BigIntegerField(db_index=True)),
                ('full_speci', models.CharField(db_index=True, max_length=254)),
                ('tree_id', models.FloatField(db_index=True)),
                ('dbhcm', models.FloatField()),
                ('abundance', models.BigIntegerField(db_index=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(db_index=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='USGrid100km',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_original', models.IntegerField(blank=True, null=True)),
                ('xmini', models.FloatField()),
                ('xmaxi', models.FloatField()),
                ('ymini', models.FloatField()),
                ('ymaxi', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(db_index=True, srid=4326)),
            ],
        ),
    ]