from django.contrib import admin
# Register your models here.
from .models import *
# from .models import MyModel

# admin.site.register(MyModel)
admin.site.register(Band)
admin.site.register(Member)

class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Genre, GenreAdmin)

