# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core import validators
# necessary data model imports
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse, reverse_lazy

class Person(models.Model):
    class Meta:
        abstract = True # declares class as abstract

    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    idnumber = models.PositiveIntegerField()
    email = models.EmailField(blank=True)
    datecreated = models.DateTimeField(blank=True, auto_now_add=True)
    datemodified = models.DateTimeField(blank=True, auto_now=True)

    # Getters for models
    @property
    def get_full_name(self):
        return f'{self.firstname} {self.lastname}'
    
    def __str__(self):
        return f'''Name: {self.get_full_name}, 
                ID Number: {self.idnumber},
                email: {self.email}'''
    


class Student(Person):
    # Must match DBMS
    CLASS_STANDING = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate')
    ]
    
    MAJORS = [
        ('CS', 'Computer Science'),
        ('ENG', 'Engineering'),
        ('SCI', 'Science'),
        ('BUS', 'Business'),
        ('LAW', 'Law'),
        ('NUR', 'Nursing'),
        ('MAT', 'Math'),
    ]

    studentid = models.PositiveIntegerField(blank=True, validators = {MinValueValidator(1)})
    classstanding = models.CharField(max_length=2, choices=CLASS_STANDING)
    major = models.CharField(max_length=3, choices=MAJORS)
    gpa = models.FloatField(blank=True, max_length=4)

    ## Getter for the url for student info
    def get_absolute_url(self):
        return reverse_lazy('regserve:students')

    ## To_String for the Student Class
    def __str__(self):
        return f'''Student ID: {self.studentid},
                {super(Student, self).__str__()}, # nnherit from Person Class
                Class Standing: {self.classstanding},
                Major: {self.major},
                GPA: {self.gpa}'''