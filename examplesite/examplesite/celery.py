import os

from celery import Celery
from celery.signals import celeryd_after_setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "examplesite.settings")

app = Celery("examplesite", broker="redis://localhost:6379/0")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()


# @celeryd_after_setup.connect
# def init_supergood(sender, instance, **kwargs):
#     print("after setup")
#     client = SGClient(
#         client_id="8330ea8603b4963155d65cac1680969d",
#         client_secret_id="3a0ac9d90cdf1589daae7a408a35e2e039a64f5b15febf1db71b47c7cba2c334",
#         base_url="https://staging-api.supergood.ai",
#         telemetry_url="https://staging-telemetry.supergood.ai",
#     )


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
