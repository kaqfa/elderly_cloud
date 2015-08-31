from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    content = models.TextField()


class Response(models.Model):
    owner = models.ForeignKey(User)
    feedback = models.ForeignKey(Feedback)
    content = models.TextField()
