from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

from member.models import Elder


class Tracker(TimeStampedModel):
    TYPE_CHOICES = (('cd', 'daily condition'), ('hr', 'heart rate'), ('bg', 'blood glucose'))
    CONDITION_CHOICES = (('1', 'tidak baik'), ('2', 'biasa'), ('3', 'baik'))

    elder = models.ForeignKey(User)
    condition = models.CharField(max_length=1, choices=CONDITION_CHOICES)
    photo = models.ImageField(null=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    value = models.IntegerField()


# class LogTracker(models.Model):
#     tracker = models.ForeignKey(Tracker)
#     value1 = models.IntegerField(default=0)
#     value2 = models.IntegerField(default=0)
#     value3 = models.IntegerField(default=0)
#     value4 = models.IntegerField(default=0)
#     value5 = models.IntegerField(default=0)