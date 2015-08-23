from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=120)
    content = models.TextField()
