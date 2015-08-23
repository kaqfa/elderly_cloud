from django.db import models
from django.contrib.auth.models import User


class Posting(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=45)
    content = models.TextField()
    category = models.CharField(max_length=45)


class PointOfInterest(models.Model):
    name = models.CharField(max_length=45)
    category = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    lattitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
