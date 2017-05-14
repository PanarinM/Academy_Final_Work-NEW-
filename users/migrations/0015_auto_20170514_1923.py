# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-14 16:23
from __future__ import unicode_literals

from django.db import migrations, models
import utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20170508_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='../static/default_img/default_user.png', upload_to=utils.get_file_path),
        ),
    ]
