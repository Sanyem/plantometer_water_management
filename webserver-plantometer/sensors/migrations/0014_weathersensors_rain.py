# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0013_auto_20171006_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathersensors',
            name='rain',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
