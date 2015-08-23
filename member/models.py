from django.db import models
from django.contrib.auth.models import User


class Elder(models.Model):
    code = models.CharField(max_length=8, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False, default='')
    cared_by = models.ManyToManyField(User, through='Caregiving')

class Caregiving(models.Model):
    user = models.ForeignKey(User)
    elder = models.ForeignKey(Elder)


class AdminInvitation(models.Model):
    user = models.ForeignKey(User)
    email_to_invite = models.CharField(max_length=45)
    status = models.CharField(max_length=1)
