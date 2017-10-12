# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import auth
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Equipment, Room, Manufacturer, Hazard
from extuser.models import ExtUser
from .forms import EquipmentForm, ManufacturerForm, RoomForm
import datetime


def home(request):
    try:
        ExtUser.objects.get(email=auth.get_user(request).email)
        equipments = Equipment.objects.all()
        return render(
            request, 'equipment/home.html',
            {
                'equipments': equipments,
                'email': auth.get_user(request).email
            }
        )
    except(KeyError):
        return redirect("login")


def list(request):
    try:
        user = ExtUser.objects.get(email=auth.get_user(request).email)
        equipments = Equipment.objects.filter(person_incharge=user)
        return render(
            request, 'equipment/list.html',
            {
                'equipments': equipments,
                'email': auth.get_user(request).email
            }
        )
    except(KeyError):
        return redirect("login")


def room_list(request):
    try:
        ExtUser.objects.get(email=auth.get_user(request).email)
        rooms = Room.objects.all()
        return render(
            request, 'equipment/rooms_list.html',
            {
                'rooms': rooms,
                'email': auth.get_user(request).email
            }
        )
    except(KeyError):
        return redirect("login")


def room_edit(request, number):
    if auth.get_user(request):
        user = ExtUser.objects.get(email=auth.get_user(request).email)
        room = get_object_or_404(Room, number=number)

        if request.method == "POST":
            form = RoomForm(request.POST, request.FILES, instance=room)

            if form.is_valid:
                room = form.save(commit=False)

                if request.FILES.get('plan'):
                    room.plan = request.FILES['plan']

                room.caution.clear()
                for name in request.POST.getlist('caution'):
                    caution = Hazard.objects.get(name=name)
                    room.caution.add(caution)

                room.save()
        else:
            form = RoomForm(instance=room)

        return render(
            request,
            'equipment/room_edit.html',
            {'room_edit_form': form, 'email': user.email, 'plan': room.plan},)
    else:
        return redirect('login')


def room_new(request):
    if auth.get_user(request):
        user = ExtUser.objects.get(email=auth.get_user(request).email)
        if request.method == "POST":
            form = RoomForm(request.POST, request.FILES)
            if form.is_valid:
                room = form.save(commit=False)
                room.number = request.POST['number']
                room.department = request.POST['department']
                room.person_incharge = ExtUser.objects.get(
                    id=request.POST['person_incharge'])
                if request.POST.get('autonomous_power') == "on":
                    room.autonomous_power = True
                else:
                    room.autonomous_power = False
                if request.FILES.get('plan'):
                    room.plan = request.FILES['plan']
                room.save()
                for name in request.POST.getlist('caution'):
                    caution = Hazard.objects.get(name=name)
                    room.caution.add(caution)
                room.save()
                return redirect('room_edit', number=room.number)
        else:
            form = RoomForm()
        return render(
            request,
            'equipment/room_new.html',
            {'room_edit_form': form, 'email': user.email})
    else:
        return redirect('login')


def mnf_list(request):
    try:
        ExtUser.objects.get(email=auth.get_user(request).email)
        manuf = Manufacturer.objects.all()
        return render(
            request, 'equipment/mnf_list.html',
            {
                'manufacturers': manuf,
                'email': auth.get_user(request).email
            }
        )
    except(KeyError):
        return redirect("login")


def mnf_edit(request, name):
    if auth.get_user(request):
        user = ExtUser.objects.get(email=auth.get_user(request).email)
        mnf = get_object_or_404(Manufacturer, name=name)
        if request.method == "POST":
            form = ManufacturerForm(request.POST, instance=mnf)
            if form.is_valid:
                mnf = form.save(commit=False)
                mnf.name = request.POST['name']
                mnf.country = request.POST['country']
                mnf.city = request.POST['city']
                mnf.mail = request.POST['mail']
                mnf.phone = request.POST['phone']
                mnf.site = request.POST['site']
                mnf.save()
        else:
            form = ManufacturerForm(instance=mnf)
        return render(
            request,
            'equipment/mnf_edit.html',
            {'mnf_edit_form': form, 'email': user.email})
    else:
        return redirect('login')


def mnf_new(request):
    if auth.get_user(request):
        user = ExtUser.objects.get(email=auth.get_user(request).email)
        if request.method == "POST":
            form = ManufacturerForm(request.POST)
            if form.is_valid:
                mnf = form.save(commit=False)
                mnf.name = request.POST['name']
                mnf.country = request.POST['country']
                mnf.city = request.POST['city']
                mnf.mail = request.POST['mail']
                mnf.phone = request.POST['phone']
                mnf.site = request.POST['site']
                mnf.save()
                return redirect('mnf_edit', name=mnf.name)
        else:
            form = ManufacturerForm()
        return render(
            request,
            'equipment/mnf_new.html',
            {'mnf_edit_form': form, 'email': user.email})
    else:
        return redirect('login')


def eq_edit(request, inv_number):
    user = ExtUser.objects.get(email=auth.get_user(request).email)
    eq_owner = Equipment.objects.get(inv_number=inv_number).person_incharge
    if user == eq_owner:
        equipment = get_object_or_404(
            Equipment,
            inv_number=inv_number)
        if request.method == "POST":
            form = EquipmentForm(request.POST, instance=equipment)
            if form.is_valid():
                equipment = form.save(commit=False)
                equipment.inv_number = request.POST['inv_number']
                equipment.ser_number = request.POST['ser_number']
                equipment.name_ru = request.POST['name_ru']
                equipment.name_en = request.POST['name_en']
                equipment.room = Room.objects.get(number=request.POST['room'])
                equipment.person_incharge = ExtUser.objects.get(
                    pk=request.POST['person_incharge'])
                if request.POST.get('service') == "on":
                    equipment.service = True
                else:
                    equipment.service = False
                year = int(request.POST['last_service_year'])
                month = int(request.POST['last_service_month'])
                day = int(request.POST['last_service_day'])
                equipment.last_service = datetime.datetime(
                    year=year, month=month, day=day)
                year = int(request.POST['next_service_year'])
                month = int(request.POST['next_service_month'])
                day = int(request.POST['next_service_day'])
                equipment.next_service = datetime.datetime(
                    year=year, month=month, day=day)
                equipment.power_wt = request.POST['power_wt']
                equipment.manufacturer = Manufacturer.objects.get(
                    name=request.POST['manufacturer'])

                equipment.save()
                return redirect('eq_edit', inv_number=equipment.inv_number)
        else:
            form = EquipmentForm(
                instance=equipment)
        return render(
            request,
            'equipment/edit.html',
            {'eq_edit_form': form, 'email': user.email})
    else:
        return redirect("list")
