"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse
from ArticalManager.forms import ArticalForm
from ArticalManager.models import Artical
from django_webtest import WebTest
class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ArticalTest(TestCase):
    def test_visit(self):
        response = self.client.get('/edit_artical/')
        self.assertEqual(response.status_code, 200)
    def test_model_create(self):
        artical = Artical();
        artical.title="testcase"
        artical.content = "this is use for test case"
        artical.volume = "case"
        artical.number = 1
        artical.save()
        localartical = Artical.objects.get(title='testcase')
        self.assertEqual(localartical.index,artical.index) 
    def test_post(self):
        artical = Artical.objects.get(title='testcase')
        artical.content = "this test case is modified"
        response =  self.client.post('/edit_artical/',{'form':artical})
        self.assertEqual(response.status_code,200) #post ok
        print Artical.objects.all()
        #self.assertEqual(articalSaved.title, artical.title)

