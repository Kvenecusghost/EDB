# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0002_auto_20170823_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='plan',
            field=models.ImageField(null=True, upload_to='pic_folder/'),
        ),
    ]
