from django.db import models
from django.contrib.auth.models import User
import datetime
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class DiseaseHist(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sudah sembuh'), ('2', 'masih diderita'))
    elder = models.ForeignKey(User)
    name = models.CharField(max_length=200, default='')
    from_year = models.IntegerField(default=0)
    to_year = models.IntegerField(default=0)


class MedicalTreatmentHist(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sudah sembuh'), ('2', 'masih diderita'))
    elder = models.ForeignKey(User)
    treatment = models.TextField()
    from_year = models.IntegerField(default=0)
    to_year = models.IntegerField(default=0)


class Note(TimeStampedModel):
    SHARABLE_CHOICES = (('1', 'yes'), ('0', 'no'))

    user = models.ForeignKey(User, related_name='by_user')
    elder = models.ForeignKey(User, related_name='for_elder')
    # daily_condition = models.ForeignKey(DailyCondition, null=True, blank=True)
    title = models.CharField(max_length=45)
    sharable = models.CharField(max_length=1, choices=SHARABLE_CHOICES, default='1')


# class Medications(models.Model):
#     elder = models.ForeignKey(Elder)
#     name = models.CharField(max_length=45)
#     dosage = models.CharField(max_length=45)
#
#
# class EmergencyContact(models.Model):
#     elder = models.ForeignKey(Elder)
#     name = models.CharField(max_length=45)
#     phone = models.CharField(max_length=45)
