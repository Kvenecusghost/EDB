# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from equipment.models import Equipment, Room, Manufacturer, Hazard

admin.site.register(Equipment)
admin.site.register(Room)
admin.site.register(Manufacturer)
admin.site.register(Hazard)
# Register your models here.
