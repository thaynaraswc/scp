# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0021_registro_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='usuario',
            new_name='user',
        ),
    ]
