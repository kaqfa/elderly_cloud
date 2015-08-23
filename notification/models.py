from django.db import models
from django.contrib.auth.models import User
from member.models import Elder


class NotificationTemplate(models.Model):
    title = models.CharField(max_length=45)
    content = models.TextField()


class Notifications(models.Model):
    elder = models.ForeignKey(Elder)
    title = models.CharField(max_length=45)
    content = models.TextField()


class EmergencyCall(models.Model):
    elder = models.ForeignKey(Elder)
    emergancy_time = models.DateTimeField()
    responded_by = models.ManyToManyField(User, null=True, blank=True,
                                          through='ResponseEmergencyCall')


class ResponseEmergencyCall(models.Model):
    user_id = models.ForeignKey(User)
    emergency_call_id = models.ForeignKey(EmergencyCall)
