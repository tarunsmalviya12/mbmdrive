# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-30 03:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drive', '0005_auto_20160730_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivefile',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
