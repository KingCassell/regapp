# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

class SimpleTest(TestCase):
    def setUp(self):
        self.test_client = Client()
    
    def test_response(self):
        response = self.test_client.get('/regserve')
        print("Inside HW test, response is {response}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Hello from backend")





# Create your tests here.
