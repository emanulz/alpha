"""
WSGI config for CotoCo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

# add the hellodjango project path into the sys.path
sys.path.append('/home/ubuntu/alpha/alpha')

# add the virtualenv site-packages path to the sys.path
sys.path.append('/home/ubuntu/venv/lib/python2.7/site-packages')

os.environ["DJANGO_SETTINGS_MODULE"] = "alpha.settings"

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
