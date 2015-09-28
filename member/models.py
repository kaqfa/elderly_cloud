from django.db import models
from django.contrib.auth.models import User
from polymorphic import PolymorphicModel
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class Member(PolymorphicModel, TimeStampedModel):
    GENDER_CHOICES = (('l', 'laki-laki'), ('p', 'perempuan'))
    user = models.OneToOneField(User)
    # name = models.CharField(max_length=100, blank=False, null=False, default='')
    address = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=20)


class CareGiver(Member):
    pass


class Partner(Member):
    pass


class Elder(Member):
    code = models.CharField(max_length=8, blank=False, null=False)
    cared_by = models.ManyToManyField(CareGiver, through='CareGiving')

    @staticmethod
    def get_cared_elder(user):
        return Elder.objects.filter(cared_by__in=[user])

    def get_kondisi(self):
        return self.dailycondition_set

    def get_kondisi_terakhir(self):
        return self.dailycondition_set.latest('id')

    def count_perawat(self):
        return self.cared_by.count()

    def get_riwayat_penyakit(self):
        return self.diseasehist_set

    def get_perawatan_medis(self):
        return self.medicaltreatmenthist_set

    def get_note(self):
        return self.note_set

    def __unicode__(self):
        return self.user.username

    def __str__(self):  # __unicode__ on Python 2
        return self.user.username


class CareGiving(TimeStampedModel):
    caregiver = models.ForeignKey(CareGiver, null=True)
    elder = models.ForeignKey(Elder, null=True)


class AdminInvitation(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sent'), ('2', 'accepted'), ('3', 'rejected'))
    user = models.ForeignKey(User)
    email_to_invite = models.CharField(max_length=45)
