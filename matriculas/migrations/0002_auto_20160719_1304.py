# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='cupo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='materia',
            name='id_materia',
            field=models.IntegerField(),
        ),
    ]