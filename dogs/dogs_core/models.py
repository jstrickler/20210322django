from django.db import models

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=32)
    breed = models.ForeignKey(Breed, on_delete = models.CASCADE)

    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    is_neutered = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.breed)


