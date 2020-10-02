from django.db import models


# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=255)
    offer = models.BooleanField(default=False)
    trip_date = models.models.DateField()
