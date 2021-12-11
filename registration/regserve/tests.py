# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
import io
from rest_framwork.parsers import JSONParser
from .serializers import *

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()
    
    def test_response(self):
        response = self.test_client.get('/regserve')
        print("Inside HW test, response is {response}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello from backend")

    def test_student_api(self):
        students_response = self.test_client.get('/regserve/data/students')
        print(f'STUDENT API TEST: inside test, response is: {students_response}\n')
        self.assertEqual(students_response.status_code, 200)
        print(f'STUDENT API TEST: inside test, response content is: {students_response.content}\n')
        student_stream = io.BytesIO(students_response.content)
        print(f'STUDENT API TEST: inside test, student stream is: {student_stream}\n')
        student_api_data = JSONParser.parse(student_stream)
        print(f'STUDENT API TEST: inside test, student api data is: {student_api_data}\n')
        first_student_data = student_api_data[0]
        print(f'STUDENT API TEST: inside test, first student data is: {first_student_data} id is {first_student_data['id']}\n')
        first_student_db = student.objects.get(id=first_student_data['id'])
        ## TODO fix this crap here
        print(f'STUDENT API TEST: inside test, response is: {students_response}\n')
        
        print(f'STUDENT API TEST: inside test, response content is: {students_response.content}\n')




# Create your tests here.
