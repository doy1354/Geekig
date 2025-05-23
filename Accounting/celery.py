"""Accounting > celery.py"""
from __future__ import absolute_import, unicode_literals
# PYTHON IMPORTS
import os
# CELERY IMPORTS
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Accounting.settings')

app = Celery('Accounting')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """debug task"""
    print('Request: {0!r}'.format(self.request))
