# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-06 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensors', '0012_auto_20171006_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservoir',
            name='actualHieght',
            field=models.FloatField(default=35),
        ),
    ]
