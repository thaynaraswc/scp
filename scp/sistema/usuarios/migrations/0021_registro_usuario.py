# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0020_auto_20161120_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
