from django.contrib import admin
# Register your models here.
from .models import Breed, Dog

# from .models import MyModel

# admin.site.register(MyModel)
admin.site.register(Breed)
admin.site.register(Dog)
