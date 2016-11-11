# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 20:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0011_auto_20161107_1700'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grupo',
            name='registro',
        ),
        migrations.AddField(
            model_name='registro',
            name='grupo',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='teste.Grupo'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='nome',
            field=models.CharField(default='Default', max_length=120),
        ),
    ]