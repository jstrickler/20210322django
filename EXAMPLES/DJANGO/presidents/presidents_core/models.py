# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Presidents(models.Model):
    termnum = models.AutoField(blank=True, primary_key=True)
    lastname = models.CharField(max_length=32, blank=True, null=True)
    firstname = models.CharField(max_length=64, blank=True, null=True)
    termstart = models.DateField(blank=True, null=True)
    termend = models.DateField(blank=True, null=True)
    birthplace = models.CharField(max_length=128, blank=True, null=True)
    birthstate = models.CharField(max_length=32, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    deathdate = models.DateField(blank=True, null=True)
    party = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = 'presidents'

    def __str__(self):
        return f"{self.termnum}: {self.firstname} {self.lastname}"
