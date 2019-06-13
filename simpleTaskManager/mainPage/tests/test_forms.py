from django.test import SimpleTestCase, TestCase
from mainPage.forms import AddTaskForm
from mainPage.models import UserMy, Project, Task
from django.contrib.auth.models import User

class TestForms(SimpleTestCase):
    
    def test_expense_form_alid_data(self):
        
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
        
        form = AddTaskForm(data = {
            'title':'TestForm',
            'description':'TESTTESTTEST',
            'due_date':'2012-09-23',
            'developer':self.testUser,
            'project':self.testProject
        })
        
        self.ssertTrue(form.is_valid())