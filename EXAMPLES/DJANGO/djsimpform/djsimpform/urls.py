"""djsimpform URL Mapping

The `urlpatterns` list maps URLs to views. More information:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Function views:
    1. Add an import:  from my_app import views
    2. Add entry to urlpatterns:  path('view_name', views.view_name, name='view_name')

Class-based views:
    1. Add an import:  from my_app.views import Home
    2. Add entry to urlpatterns:  path('view_name', ViewName.as_view(), name='view_name')

Including another (usually an app's) URLconf:
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  path('appname', include('app.urls', namespace="app"))
    Path may be blank; in that case only the app URL is used

    -----------------------------------------------------------------------------------
    NOTE: when using the namespace argument with include(), the app's urls.py MUST have

        app_name="APPNAME"

    before  urlpatterns = ...
    -----------------------------------------------------------------------------------
"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('simpform.urls', namespace="simpform")),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

