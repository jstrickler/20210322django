from uuid import uuid4
from django.db import models


class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text="Unique ID of this city")
    name = models.CharField(max_length=64, help_text="City name")
    admindiv = models.CharField(max_length=128, help_text="Administrative Division (State/Province etc.)", null=True)
    country = models.CharField(max_length=2, help_text="Country code", default="US")

    class Meta:
        db_table = 'cities'
        verbose_name_plural = 'cities'

    def __str__(self):
        return f"{self.name}, {self.admindiv}"


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, help_text="Unique ID of this contact")
    first_name = models.CharField(max_length=32, help_text="First name")
    last_name = models.CharField(max_length=32, help_text="Last name")
    street_address = models.CharField(max_length=32, help_text="Street address", null=True)
    postcode = models.CharField(max_length=16, help_text="Postal code (Zip, etc)", null=True)
    dob = models.DateField(help_text="Date of birth", null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True,
                             related_name="cities", help_text="City for this contact")
    title = models.CharField(max_length=8, help_text="Title", null=True)

    class Meta:
        db_table = 'contacts'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
