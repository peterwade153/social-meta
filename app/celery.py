from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

from utils.read_envs import read_env_file


# set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
# Either user local or prod settings
if 'ENV_VAR_FILE' in os.environ:
    file_name = os.getenv('ENV_VAR_FILE')
    read_env_file(file_name)

REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
app = Celery('app', broker=REDIS_URL)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.update(
    worker_max_tasks_per_child=1,
    broker_pool_limit=None
)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
