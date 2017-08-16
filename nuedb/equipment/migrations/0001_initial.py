# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-16 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('department', models.CharField(max_length=64)),
                ('mobile_phone', models.CharField(max_length=11)),
                ('job_phone', models.CharField(max_length=4)),
                ('room', models.CharField(max_length=5)),
                ('mail', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=25)),
            ],
        ),
    ]