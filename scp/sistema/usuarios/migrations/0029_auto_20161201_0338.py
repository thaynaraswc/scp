# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0028_remove_registro_grupo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='movimentacao',
            name='item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Movimentacao',
        ),
        migrations.DeleteModel(
            name='Tipo',
        ),
    ]
