# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-26 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170309_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='edit_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='edit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
