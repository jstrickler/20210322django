from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Member(models.Model):
    name = models.CharField(max_length=64)
    # last_name = models.CharField(max_length=64)
    #
    # class Meta: # Model config
    #     unique_together = ['first_name', 'last_name']

    def __str__(self):
        return self.name


class Band(models.Model):
    name = models.CharField(max_length=32)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    members = models.ManyToManyField(Member, related_name='bands')   # creates table bands_members

    def __str__(self):
        return self.name
