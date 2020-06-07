from __future__ import absolute_import
import os
from celery import Celery
from celaryapp.settings import BROKER_URL, BACKEND_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE','celaryapp.settings')

from django.conf import settings

app = Celery('celaryapp', broker=BROKER_URL, backend=BACKEND_URL)
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

if __name__ == '__main__':
    debug_task.delay()
