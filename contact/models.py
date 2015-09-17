from django.db import models
from django.contrib.auth.models import User

from member.models import Elder


class Contact(models.Model):
    """
    Elder contact list
    """
    elder = models.ForeignKey(Elder)
    added_by = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=25)
    email = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=1)