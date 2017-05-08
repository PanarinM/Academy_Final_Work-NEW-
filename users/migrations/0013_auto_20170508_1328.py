# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-08 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20170508_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=utils.get_file_path),
        ),
    ]
