import uuid
from django.db import models

class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")
    abbr = models.CharField(max_length=4, null=True, help_text="Abbreviation of breed name")

    name = models.CharField(max_length=64, help_text="Name of breed")

    class Meta:
        db_table = 'breeds'

    def __str__(self):
        return self.name

class Dog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")
    name = models.CharField(max_length=64, help_text="Name of dog")
    sex = models.CharField(max_length=1, choices=[('f', 'Female'), ('m', 'Male')], help_text="Sex of dog (m or f)")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, related_name="breeds", help_text="Breed of dog")
    is_neutered = models.BooleanField(default=False, help_text="Whether dog is neutered")
    weight  = models.IntegerField(help_text="Approximate weight of dog in pounds")

    class Meta:
        db_table = 'dogs'

    def __str__(self):
        return f"{self.name} ({self.breed})"
