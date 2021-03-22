from django.contrib import admin
# Register your models here.

from .models import City, Contact

admin.site.register(City)
admin.site.register(Contact)
