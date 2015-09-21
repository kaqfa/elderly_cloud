from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel


class Feedback(TimeStampedModel, StatusModel):
    STATUS = Choices(('s', 'sent'), ('r', 'responded'), ('c', 'closed'))
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=120, default='')
    content = models.TextField(default='')


class Response(models.Model):
    owner = models.ForeignKey(User)
    feedback = models.ForeignKey(Feedback)
    content = models.TextField(default='')
