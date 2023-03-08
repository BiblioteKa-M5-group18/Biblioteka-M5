from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteka.settings')

app = Celery('biblioteka')

app.config_from_object('django.config:settings', namespace='CELERY')

app.autodiscover_tasks()