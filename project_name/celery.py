import os

from django.conf import settings  # noqa

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{ project_name }}.settings')


app = Celery('{{ project_name }}')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print(('Request: {0!r}'.format(self.request)))
