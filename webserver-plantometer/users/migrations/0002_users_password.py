# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-15 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
