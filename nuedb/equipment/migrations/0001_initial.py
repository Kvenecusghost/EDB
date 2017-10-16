# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 04:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('inv_number', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('ser_number', models.CharField(blank=True, max_length=32, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=128, null=True)),
                ('name_en', models.CharField(blank=True, max_length=128, null=True)),
                ('manual', models.FileField(blank=True, null=True, upload_to=b'')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('service', models.BooleanField(default=True)),
                ('last_service', models.DateField(blank=True, null=True)),
                ('next_service', models.DateField(blank=True, null=True)),
                ('power_wt', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'permissions': (('can_view', '\u041c\u043e\u0436\u0435\u0442 \u043f\u0440\u043e\u0441\u043c\u0430\u0442\u0440\u0438\u0432\u0430\u0442\u044c'),),
            },
        ),
        migrations.CreateModel(
            name='Hazard',
            fields=[
                ('name', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('image', models.ImageField(null=True, upload_to='rooms/hazard/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=16, null=True)),
                ('site', models.URLField(blank=True, max_length=32, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('block', models.CharField(blank=True, max_length=16, null=True)),
                ('department', models.CharField(blank=True, max_length=64, null=True)),
                ('room_type', models.CharField(blank=True, max_length=32, null=True)),
                ('autonomous_power', models.BooleanField(default=False)),
                ('electricity', models.CharField(blank=True, max_length=64, null=True)),
                ('gases', models.CharField(blank=True, max_length=64, null=True)),
                ('ventilation', models.CharField(blank=True, max_length=64, null=True)),
                ('water', models.CharField(blank=True, max_length=64, null=True)),
                ('clean_room', models.CharField(blank=True, max_length=64, null=True)),
                ('plan', models.ImageField(null=True, upload_to='rooms/plan/%Y/%m/%d')),
                ('caution', models.ManyToManyField(to='equipment.Hazard')),
                ('person_incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Room.person_incharge+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipment.Manufacturer'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='person_incharge',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Equipment.person_incharge+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='equipment',
            name='room',
            field=models.ForeignKey(blank=True, max_length=5, null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.Room'),
        ),
    ]
