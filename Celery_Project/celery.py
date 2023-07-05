from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Celery_Project.settings')

app = Celery('Celery_Project')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Karachi')


app.config_from_object(settings, namespace='CELERY')

# Celery Beat Settings
app.conf.beat_schedule = {
    'send-mail-every-day-at-8': {
        'task': 'home.tasks.send_mail_func',
        'schedule': crontab(hour=18, minute=50, day_of_month=19, month_of_year = 6),
        'args': (2,)
    }
    
}


app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')