# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 13:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0004_auto_20160719_1308'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materia',
            name='id_materia',
        ),
    ]
