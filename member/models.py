from django.db import models
from django.contrib.auth.models import User


class Elder(models.Model):
    code = models.CharField(max_length=8, blank=False, null=False)
    name = models.CharField(max_length=100, blank=False, null=False, default='')
    address = models.TextField(null=True, blank=True)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=1)
    phone = models.CharField(max_length=20)
    cared_by = models.ManyToManyField(User, through='Caregiving')

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
        return self.name

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Caregiving(models.Model):
    user = models.ForeignKey(User)
    elder = models.ForeignKey(Elder)


class AdminInvitation(models.Model):
    user = models.ForeignKey(User)
    email_to_invite = models.CharField(max_length=45)
    status = models.CharField(max_length=1)
