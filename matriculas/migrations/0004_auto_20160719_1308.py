# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-19 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matriculas', '0003_auto_20160719_1307'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='nombres',
            new_name='nombre',
        ),
    ]
