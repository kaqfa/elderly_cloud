from django.db import models

from member.models import Elder


class TrackerTemplate(models.Model):
    name = models.CharField(max_length=45, blank=False, default='')
    field1 = models.CharField(max_length=45)
    field2 = models.CharField(max_length=45)
    field3 = models.CharField(max_length=45)
    field4 = models.CharField(max_length=45)
    field5 = models.CharField(max_length=45)


class Tracker(models.Model):
    elder = models.ForeignKey(Elder)
    name = models.CharField(max_length=45, blank=False, default='')
    field1 = models.CharField(max_length=45)
    field2 = models.CharField(max_length=45)
    field3 = models.CharField(max_length=45)
    field4 = models.CharField(max_length=45)
    field5 = models.CharField(max_length=45)


class LogTracker(models.Model):
    tracker = models.ForeignKey(Tracker)
    value1 = models.IntegerField(default=0)
    value2 = models.IntegerField(default=0)
    value3 = models.IntegerField(default=0)
    value4 = models.IntegerField(default=0)
    value5 = models.IntegerField(default=0)
