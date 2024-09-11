from django.db import models


# Create your models here.


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    # describtion = models.CharField(max_length=400)
    # img = models.CharField(max_length=50)

    def __str__(self):
        return self.name
