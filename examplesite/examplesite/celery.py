import os

from celery import Celery
from celery.signals import celeryd_after_setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examplesite.settings")

app = Celery("examplesite", broker="redis://localhost:6379/0")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# @celeryd_after_setup.connect
# def init_supergood(sender, instance, **kwargs):
#     client = SGClient()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
