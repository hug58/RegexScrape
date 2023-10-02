""" config celery"""
import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "regex_scrape.settings")

app = Celery("regex_scrape")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """ task to debug"""
    print(f'Request: {self.request!r}')
