from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'unity_test.settings')
app = Celery('unity_test')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    # Executes everynight at 11:00 p.m.
    'send-email-every-monday-wednesday-task': {
        'task': 'send_email_to_all_users',
        'schedule': crontab(minute=0, hour=23, day_of_week='mon,wed'),
    },
}
app.conf.timezone = 'UTC'

app.autodiscover_tasks()
