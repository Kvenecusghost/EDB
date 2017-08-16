# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
	name = models.CharField(max_length=32)
	surname = models.CharField(max_length=32)
	department = models.CharField(max_length=64)
	mobile_phone = models.CharField(max_length=11)
	job_phone = models.CharField(max_length=4)
	room = models.CharField(max_length=5)
	mail = models.EmailField()
	position = models.CharField(max_length=25)	

class Manufacturers(models.Model):
	name = models.CharField(primary_key=True, max_length=64)
	country = models.CharField(max_length=32, default='')
	city = models.CharField(max_length=32, default='')
	mail = models.EmailField(default='blank@blank.com')
	phone = models.CharField(max_length=16, default='')
	site = models.URLField(max_length=32, default='blank.com')

class Rooms(models.Model):
	number = models.CharField(primary_key=True, max_length=5)
	department = models.CharField(max_length=64)
	person_incharge = models.ForeignKey('Users', on_delete=models.SET_DEFAULT, default=0)
	autonomous_power = models.BooleanField(default=True)
	power_wt = models.IntegerField(default=0)
	room_type = models.CharField(max_length=32,default='')

class Equipments(models.Model):
	inv_number = models.CharField(primary_key=True, max_length=16)
	ser_number = models.CharField(max_length=32)
	name_ru = models.CharField(max_length=128)
	name_en = models.CharField(max_length=128)
	room = models.ForeignKey('Rooms',max_length=5,null=True)
	manual = models.FileField(default=0)
	photo = models.FileField(default=0)
	person_incharge = models.ForeignKey('Users', on_delete=models.SET_DEFAULT, default=0)
	service = models.BooleanField(default=True)
	last_service = models.DateField(null=True)
	next_service = models.DateField(null=True)
	power_wt = models.IntegerField(default=0)
	manufacturer = models.ForeignKey('Manufacturers',on_delete=models.SET_DEFAULT, default=0)

	
