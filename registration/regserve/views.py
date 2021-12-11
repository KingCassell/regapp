# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_frameworks import generics
from .serializers import *
from django.views.generic import ListView, CreateView

# Create your views here.


def index(request):
    return HttpResponse("Hello from backend")

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer()

class StudentListForm(ListView):
    model = Student

class StudentCreateForm(CreateView, ListView):
    model = Student
    fields = ['firstname', 'lastname', 'idnumber', 'classstanding', 'major', 'gpa']