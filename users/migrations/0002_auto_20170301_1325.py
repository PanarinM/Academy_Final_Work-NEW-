# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[users.models.validate_phone]),
        ),
    ]
