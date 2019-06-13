from django.test import TestCase, Client
from django.urls import reverse,resolve
from mainPage.models import UserMy, Project, Task
from django.contrib.auth.models import User
import datetime
import json


class TestViews(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.mainPage_url = reverse('mainPage')
        self.addTask_url = reverse('addTask')
        self.deleteTask_url = reverse('deleteTask')
        self.editTask_url = reverse('editTask' ,args=['testTask'])
        self.compliteTask_url = reverse('compliteTask' ,args=['testTask'])
        
        self.user = User.objects.create_user(
            'Nikolay', 
            'qwe@gmail.com', 
            'qwe'
        )
        
        self.testUser = UserMy.objects.create(
            user = self.user,
            user_role = 'developer'
        )
        
        self.testProject = Project.objects.create(
            project_name = 'TestProject'
        )
        
        self.testProject.users.add(self.testUser)
        
        self.testTask = Task.objects.create(
            title = 'testTask',
            description = 'testtesttest',
            due_date = datetime.datetime.now().strftime("%Y-%m-%d"),
            project = self.testProject,
            developer = self.testUser,
            status = False
        )

    def test_main(self):
        response = self.client.get(self.mainPage_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'mainPage/mainPage.html')
    
    def test_addTask(self):
        response = self.client.get(self.addTask_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'mainPage/form.html')
    

        