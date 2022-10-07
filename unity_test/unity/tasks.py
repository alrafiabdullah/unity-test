import random
import string

from .models import EmailSubscription
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage

from celery import shared_task

from unity_test.celery import app


@shared_task
def create_random_email_subscriber(total):
    if total < 1 or total > 1000:
        return 'Please select a number between 1 and 1000'
    for i in range(total):
        first_name = '{}'.format(
            get_random_string(random.randint(3, 6), string.ascii_letters))
        last_name = '{}'.format(
            get_random_string(random.randint(3, 6), string.ascii_letters))
        email = '{}@{}.com'.format(first_name, last_name)
        is_subscribed = random.choice([True, False])
        EmailSubscription.objects.create(
            email=email, is_subscribed=is_subscribed)
    return '{} random email subscribers created with success!'.format(total)


@app.task(name="send_email_to_all_users", bind=True, default_retry_delay=300, max_retries=3)
def send_email_to_all_users(self):
    try:
        all_users = EmailSubscription.objects.filter(is_subscribed=True)
        # send email to all users
        for user in all_users:
            email = EmailMessage(
                subject='Hello',
                body='This is a test email',
                from_email='',
                to=[user.email],
            )
            email.send()

    except:
        send_email_to_all_users.retry()

    return f'All users ({all_users.count()}) email sent successfully!'
