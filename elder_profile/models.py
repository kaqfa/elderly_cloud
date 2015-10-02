import datetime

from django.db import models
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from member.models import Elder, CareGiver


class DiseaseHist(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sudah sembuh'), ('2', 'masih diderita'))
    elder = models.ForeignKey(Elder, verbose_name='Orang Tua')
    name = models.CharField('Nama Penyakit', max_length=200, default='')
    from_year = models.IntegerField('Dari Tahun', default=datetime.date.today().year)
    to_year = models.IntegerField('Hingga Tahun', default=datetime.date.today().year)

    class Meta:
        verbose_name_plural = 'Riwayat Penyakit'
        verbose_name = 'Riwayat Penyakit'


class MedicalTreatmentHist(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sudah sembuh'), ('2', 'masih diderita'))
    elder = models.ForeignKey(Elder, verbose_name='Orang Tua')
    treatment = models.TextField('Nama Penanganan')
    from_year = models.IntegerField('Dari Tahun', default=0)
    to_year = models.IntegerField('Hingga Tahun', default=0)

    class Meta:
        verbose_name = 'Penanganan Kesehatan'
        verbose_name_plural = 'Riwayat Treatment'


class Note(TimeStampedModel):
    SHARABLE_CHOICES = (('1', 'Iya'), ('0', 'Tidak'))

    user = models.ForeignKey(CareGiver, related_name='by_user', verbose_name='Penulis Catatan')
    elder = models.ForeignKey(Elder, related_name='for_elder', verbose_name='Orang Tua')
    # daily_condition = models.ForeignKey(DailyCondition, null=True, blank=True)
    title = models.CharField('Judul Catatan', max_length=45)
    content = models.TextField('Isi Catatan', default='')
    sharable = models.CharField('Dapat Dibagikan', max_length=1,
                                choices=SHARABLE_CHOICES, default='1')

    class Meta:
        verbose_name = 'Catatan'
        verbose_name_plural = 'Data Catatan'


# class Medications(models.Model):
# elder = models.ForeignKey(Elder)
# name = models.CharField(max_length=45)
#     dosage = models.CharField(max_length=45)
#
#
# class EmergencyContact(models.Model):
#     elder = models.ForeignKey(Elder)
#     name = models.CharField(max_length=45)
#     phone = models.CharField(max_length=45)
