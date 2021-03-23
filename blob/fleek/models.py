from django.db import models

class City(models.Model):
    name = models.CharField(max_length=32)

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=16)
    last_name = models.CharField(max_length=16)
    dob = models.DateField()
    favorite_color = models.CharField(max_length=16)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
