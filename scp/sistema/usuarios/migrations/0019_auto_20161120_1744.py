# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0018_auto_20161111_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo',
            name='item',
        ),
        migrations.AddField(
            model_name='item',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teste.Tipo'),
        ),
    ]