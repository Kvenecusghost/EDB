# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 08:27
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_auto_20170922_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='caution',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('biohazard', 'Biohazard'), ('flamable', 'Flamable'), ('burstable', 'Burstable'), ('poisonous', 'Poisonous'), ('acid', 'Acid'), ('highvoltage', 'High voltage')], max_length=55, null=True),
        ),
    ]
