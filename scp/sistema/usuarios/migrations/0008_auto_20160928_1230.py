# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_auto_20160928_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='cpf',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
