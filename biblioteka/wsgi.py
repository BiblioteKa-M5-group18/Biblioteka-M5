import os

from django.core.wsgi import get_wsgi_application

from django_apscheduler.jobstores import register_events

from followings.tasks import scheduler

application = get_wsgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteka.settings")


register_events(scheduler)
