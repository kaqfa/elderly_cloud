from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from member.models import Elder


class NotificationTemplate(models.Model):
    LEVEL_CHOICES = (('1', 'info'), ('2', 'warning'), ('3', 'emergency'))
    title = models.CharField(max_length=45)
    content = models.TextField()
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)


class Notification(TimeStampedModel, StatusModel):
    STATUS = Choices(('s', 'sent'), ('r', 'responded'))
    LEVEL_CHOICES = (('1', 'info'), ('2', 'warning'), ('3', 'emergency'))
    RECUR_CHOICES = (('1', 'sekali'), ('2', 'harian'), ('3', 'mingguan'),
                     ('4', 'bulanan'), ('5', 'weekday'), ('6', 'weekend'))

    title = models.CharField(max_length=45)
    content = models.TextField()
    invoked_on = models.DateTimeField(null=True, blank=True)
    recurring = models.CharField(max_length=1, choices=RECUR_CHOICES)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    sender = models.ForeignKey(User, related_name='notif_sender')
    receiver = models.ForeignKey(User, related_name='notif_receiver')
    responded = models.ManyToManyField(User, blank=True, through='ResponseNotification')
    # tidak perlu null = True


class ResponseNotification(TimeStampedModel):
    user_id = models.ForeignKey(User)
    notification_id = models.ForeignKey(Notification)
