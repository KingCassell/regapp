# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import validators

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django.urls import reverse, reverse_lazy


class Student(models.Model):
    studentid = models.PositiveIntegerField(blank=True, validators = {MinValueValidator(1)})




# Create your models here.

def get_absolute_url(self):
    return reverse_lazy('regserve:students')