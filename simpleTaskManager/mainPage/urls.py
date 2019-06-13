from django.urls import include, path
#from mainPage.views import main,addTaskForm,deleteTask_view,compliteTask_view,editTask_view
from .views import *
urlpatterns = [
    path('', main, name='mainPage'),
    path('addTask/',addTaskForm,name='addTask'),
    path('deleteTask/',deleteTask_view,name='deleteTask'),
    path('editTask/<task_id>',editTask_view,name='editTask'),
    path('compliteTask/<task_id>',compliteTask_view,name='compliteTask'),
]
