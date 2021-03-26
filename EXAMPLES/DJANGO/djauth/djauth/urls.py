"""djauth URL Mapping

"""
from django.conf import settings
from django.urls import path, include
from django.contrib import admin

# site-wide route mapping
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('superheroes.urls', namespace="superheroes")),  # delegate to app's URL config
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

