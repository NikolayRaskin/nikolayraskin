from django.test import SimpleTestCase
from django.urls import reverse,resolve
from mainPage.views import *

class TestUrls(SimpleTestCase):
    
    def test_url_main(self):
        url = reverse('mainPage')
        print(resolve(url))
        self.assertEquals(resolve(url).func,main)
        
    def test_url_addTask(self):
        url = reverse('addTask')
        print(resolve(url))
        self.assertEquals(resolve(url).func,addTaskForm)
        
    def test_url_deleteTask(self):
        url = reverse('deleteTask')
        print(resolve(url))
        self.assertEquals(resolve(url).func,deleteTask_view)
        
    def test_url_editTask(self):
        url = reverse('editTask',args=['some_url'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,editTask_view)
        
    def test_url_compliteTask(self):
        url = reverse('compliteTask',args=['some_url'])
        print(resolve(url))
        self.assertEquals(resolve(url).func,compliteTask_view)
          