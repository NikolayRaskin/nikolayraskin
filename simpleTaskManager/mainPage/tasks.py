from celery.registry import tasks
from celery.task import Task
#from django.conf import settings
from django.core.mail import send_mail
from celery.task import periodic_task
from celery.schedules import crontab
from .models import UserMy,Project,Task

@periodic_task(ignore_result=True, run_every=60)
class SignUpTask(Task):
    
    def run(self):
        print('IT\'S A TRAP')
        taskskQuery = Task.objects.all()
        subject = 'New task for' + str(taskskQuery[0].developer.user.username)
        message = 'There is new task for you.'
        email_from = 'nikolay.raskin98@gmail.com'
        recipient_list = [taskskQuery[0].developer.user.email,]
        send_mail( subject, message, email_from, recipient_list )

tasks.register(SignUpTask)