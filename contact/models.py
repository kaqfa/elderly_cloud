from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from member.models import Elder, CareGiver


class Contact(TimeStampedModel, StatusModel):
    """
    Elder contact list
    """
    STATUS = Choices(('1', 'aktif'), ('2', 'non aktif'))

    elder = models.ForeignKey(Elder, verbose_name='Kontak untuk')
    added_by = models.ForeignKey(CareGiver, verbose_name='Ditambahkan oleh')
    name = models.CharField(max_length=100, default='', verbose_name='Nama Kontak')
    address = models.CharField(max_length=200, null=True, blank=True,
                               verbose_name='Alamat Kontak')
    phone = models.CharField(max_length=25, default='', verbose_name='Telepon Kontak')
    email = models.CharField(max_length=255, null=True, blank=True,
                             verbose_name='Email Kontak')

    class Meta:
        verbose_name = 'Kontak'
        verbose_name_plural = 'Data Kontak'