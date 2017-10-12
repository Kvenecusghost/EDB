# -*- coding: utf-8 -*-

u"""Classes for extended Django user model."""

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):

    u"""Default class for models managing."""

    def create_user(self, email, password=None):
        u"""
        Create ExtUser. Email (default) is required.

        You can override required field here and in ExtUser model.
        """
        if not email:
            raise ValueError('Email is required.')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        u"""Create superuser."""
        user = self.create_user(email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):
    u"""
    Default ExtUser model for replacing default User model.

    You must make all changes, definition additional fields and other here.

    !!! WARNING !!!
    Field avatar require installed Pillow module!
    """

    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
        db_index=True
    )
    firstname = models.CharField(
        'First name',
        max_length=40,
    )
    lastname = models.CharField(
        'Last name',
        max_length=40,
    )
    department = models.CharField(
        'Department',
        max_length=64,
        null=True,
        blank=True
    )
    position = models.CharField(
        'Position',
        max_length=25,
        null=True,
        blank=True
    )
    mobile_phone = models.CharField(
        'Mobile Phone',
        max_length=11,
        null=True,
        blank=True
    )
    job_phone = models.CharField(
        'Job Phone',
        max_length=4,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        'Date of birth',
        null=True,
        blank=True
    )
    register_date = models.DateField(
        'Registration date',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Active',  # Not blocked, banned, etc
        default=True
    )
    is_admin = models.BooleanField(
        'Is superuser',
        default=False
    )

    # Django require define this method
    def get_full_name(self):
        return self.email

    @property
    def is_staff(self):
        # Required Django for admin panel
        return self.is_admin

    def get_short_name(self):
        u"""Return short name."""
        return self.email

    def __str__(self):
        u"""String representation of model. Email by default."""
        return "%s: %s %s" % (self.email, self.firstname, self.lastname)

    def __unicode__(self):
        return "%s %s" % (self.firstname, self.lastname)

    # Field, used as 'username' in authentication and orher forms
    USERNAME_FIELD = 'email'

    """
    Username required by default. Add here another fields, where
    must be defined for correct model creation.
    """
    REQUIRED_FIELDS = []

    # Link model and model manager
    objects = UserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'extuser'
