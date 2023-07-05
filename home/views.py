from django.shortcuts import render,HttpResponse
from .tasks import test_func
from send_mail_app.tasks import send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json

from .tasks import sleepy

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")
# Runing Clery Project
#   celery -A Celery_Project.celery worker  --pool=solo -l info#
# celery -A Celery_Project beat -l INFO
#pip install -U django-celery-results


def send_mail_to_all(request):
    send_mail_func.delay()
    return HttpResponse("Sent")


def schedule_mail(request):
    schedule, created = CrontabSchedule.objects.get_or_create(hour = 1, minute = 34)
    task = PeriodicTask.objects.create(crontab=schedule, name="schedule_mail_task_"+"5", task='home.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return HttpResponse("Done")

def index(request):
    sleepy(11)
    return HttpResponse("<h1>success</h1>")
