from django.db import models
from django.contrib.auth.models import User

from member.models import Elder


class DiseaseHist(models.Model):
    elder = models.ForeignKey(Elder)
    name = models.CharField(max_length=200, default='')
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    status = models.CharField(max_length=1)


class MedicalTreatmentHist(models.Model):
    elder = models.ForeignKey(Elder)
    treatment = models.TextField()
    from_year = models.IntegerField()
    to_year = models.IntegerField()
    status = models.CharField(max_length=1)


class Note(models.Model):
    user = models.ForeignKey(User)
    elder = models.ForeignKey(Elder)
    # daily_condition = models.ForeignKey(DailyCondition, null=True, blank=True)
    title = models.CharField(max_length=45)


class Medications(models.Model):
    elder = models.ForeignKey(Elder)
    name = models.CharField(max_length=45)
    dosage = models.CharField(max_length=45)


class EmergencyContact(models.Model):
    elder = models.ForeignKey(Elder)
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
