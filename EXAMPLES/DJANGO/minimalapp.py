"""
Unrealistically minimum Django app. Combines manage.py, settings.py, views.py, and urls.py into a single file.

Note: Not recommended for real-world apps.
"""
import os
import sys
from django.urls import path
from django.http import HttpResponse

SECRET_KEY = 's3cr3t'
DEBUG = True
ROOT_URLCONF = 'minimalapp'

def hello(request):
    return HttpResponse("Hello really minimal Django world")

urlpatterns = [ path('', hello) ]

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "minimalapp")
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
