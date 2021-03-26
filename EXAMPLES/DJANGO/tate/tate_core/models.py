import uuid
from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    tate_id = models.IntegerField(default=0)
    name = models.CharField(max_length=256, help_text="Artist's full name")
    place_of_birth = models.CharField(null=True, max_length=256, help_text="Location of artist's birth")
    birth_year = models.IntegerField(null=True, help_text="Year the artist was born")
    death_year = models.IntegerField(null=True, help_text="Year the artist died")
    tate_url = models.URLField(null=True, help_text="Link to this artist at www.tate.org.uk")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text="Unique ID of this artist")

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=512, default=None, help_text="Title of the artwork")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True,
                               related_name="artworks", help_text="Artist who created this artwork")
    date_text = models.CharField(max_length=64, help_text="Date artwork was completed (if known)")
    thumbnail_url = models.URLField(help_text="Link to a thumbnail of this artwork at www.tate.org.uk")
    tate_url = models.URLField(help_text="Link to a full image of this artwork at www.tate.org.uk")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,help_text="Unique ID of this artwork")

    def __str__(self):
        return f"{self.title} by {self.artist}"
