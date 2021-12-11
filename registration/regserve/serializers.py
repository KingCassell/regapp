from django.db.models import fields
from rest_framework import serializers
from .models import *

class StudenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = {}

    def create():



