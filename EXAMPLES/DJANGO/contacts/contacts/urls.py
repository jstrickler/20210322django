from django.conf import settings
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin', admin.site.urls),
    # path('dogs', include('contacts_core.urls', namespace="dogs_core")),
    # path('art', include('contacts_core.urls', namespace="art_core")),
    path('', include('contacts_core.urls', namespace="contacts")),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

# include Django Debug toolbar if DEBUG is set
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns

# 3f2540e4b1bf996c396e04c5463a47e42900441a
