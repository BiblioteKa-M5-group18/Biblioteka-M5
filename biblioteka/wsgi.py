import os

import django

from django.core.wsgi import get_wsgi_application

from django_apscheduler.jobstores import register_events

from followings.tasks import scheduler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteka.settings")

django.setup()

application = get_wsgi_application()


register_events(scheduler)
