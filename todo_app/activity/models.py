from django.db import models

# Create your models here.
class Activity(models.Model):
    author = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.CharField(max_length=255)
    city = models.CharField(max_length=255)