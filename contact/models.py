from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from member.models import Elder, CareGiver


class Contact(TimeStampedModel, StatusModel):
    """
    Elder contact list
    """
    STATUS = Choices(('1', 'aktif'), ('2', 'non aktif'))

    elder = models.ForeignKey(Elder)
    added_by = models.ForeignKey(CareGiver)
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=25, default='')
    email = models.CharField(max_length=255, null=True, blank=True)