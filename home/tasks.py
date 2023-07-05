from celery import shared_task
from time import sleep
from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from Celery_Project import settings
from django.utils import timezone
from datetime import timedelta

#celery multi restart w1 -A Celery_Project -l info  # restart workers


@shared_task(bind=True)
def send_mail_func(self):
    users = get_user_model().objects.all()
    #timezone.localtime(users.date_time) + timedelta(days=2)
    for user in users:
        mail_subject = "Mr Rashid"
        message="hi i am Rashid Khan"
     #   message = "hi I am Rashid Khan this is for celery Project i am testin my celery project please ignore it"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return "Done"

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"
def sleepy(duration):
    sleep(duration)
    return None
