# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 21:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0022_auto_20161122_1641'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='adress',
            new_name='endereco',
        ),
    ]
