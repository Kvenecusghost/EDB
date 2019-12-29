# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from extuser.models import ExtUser


class Manufacturer(models.Model):
    name = models.CharField(
        primary_key=True,
        max_length=64
    )
    country = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=32,
        null=True,
        blank=True)
    mail = models.EmailField(
        null=True,
        blank=True
    )
    phone = models.CharField(
        max_length=16,
        null=True,
        blank=True
    )
    site = models.URLField(
        max_length=32,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return self.name


class Hazard(models.Model):
    name = models.CharField(
        max_length=12,
        primary_key=True
    )
    image = models.ImageField(
        upload_to='rooms/hazard/%Y/%m/%d',
        null=True,
    )

    def __unicode__(self):
        return "%s" % (self.name)


class Room(models.Model):
    number = models.CharField(
        primary_key=True,
        max_length=5
    )
    block = models.CharField(
        max_length=16,
        null=True,
        blank=True,
    )
    department = models.CharField(
        max_length=64,
        null=True,
        blank=True,
    )
    room_type = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )
    person_incharge = models.ForeignKey(
        ExtUser,
        related_name='Room.person_incharge+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    autonomous_power = models.BooleanField(
        default=False,
        blank=True
    )
    electricity = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )
    gases = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )
    ventilation = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )
    water = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )
    clean_room = models.CharField(
        null=True,
        blank=True,
        max_length=64,
    )
    plan = models.ImageField(
        upload_to='rooms/plan/%Y/%m/%d',
        null=True,
    )
    caution = models.ManyToManyField(
        'Hazard',
    )

    def __unicode__(self):
        return self.number


class Equipment(models.Model):
    inv_number = models.CharField(
        primary_key=True,
        max_length=16
    )
    ser_number = models.CharField(
        max_length=32,
        null=True,
        blank=True
    )
    name_ru = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    name_en = models.CharField(
        max_length=128,
        null=True,
        blank=True
    )
    room = models.ForeignKey(
        'Room',
        max_length=5,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    manual = models.FileField(
        null=True,
        blank=True
    )
    photo = models.ImageField(
        null=True,
        blank=True
    )
    person_incharge = models.ForeignKey(
        ExtUser,
        related_name='Equipment.person_incharge+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    service = models.BooleanField(
        default=True,
        blank=True
    )
    last_service = models.DateField(
        null=True,
        blank=True
    )
    next_service = models.DateField(
        null=True,
        blank=True
    )
    power_wt = models.IntegerField(
        null=True,
        blank=True
    )
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __unicode__(self):
        return "%s %s/%s" % (self.inv_number, self.name_en, self.name_ru)

    class Meta:
        permissions = (
            ("can_view", "Может просматривать"),
        )
