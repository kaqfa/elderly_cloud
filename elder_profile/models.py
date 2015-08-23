from django.db import models
from django.contrib.auth.models import User

from member.models import Elder


class DiseaseHist(models.Model):
	elder = models.ForeignKey(Elder)
	disease = models.CharField(max_length=45)


class MedicalTreatmentHist(models.Model):
	elder = models.ForeignKey(Elder)
	treatment = models.TextField()


class DailyCondition(models.Model):
	elder = models.ForeignKey(Elder)
	condition = models.CharField(max_length=1)
	time_record = models.DateTimeField()


class Note(models.Model):
	user = models.ForeignKey(User)
	elder = models.ForeignKey(Elder)
	title = models.CharField(max_length=45)


class Medications(models.Model):
	elder = models.ForeignKey(Elder)
	name = models.CharField(max_length=45)
	dosage = models.CharField(max_length=45)


class EmergencyContact(models.Model):
    elder = models.ForeignKey(Elder)
    name = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
