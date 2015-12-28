from django.db import models
from django.contrib.auth.models import User
from polymorphic import PolymorphicModel
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

def get_unread_notif(self):
    return self.notif_receiver.filter(status='s').order_by('-invoked_on', '-modified')

User.add_to_class('get_unread_notif', get_unread_notif)
    
class Member(PolymorphicModel, TimeStampedModel):
    GENDER_CHOICES = (('l', 'laki-laki'), ('p', 'perempuan'))
    user = models.OneToOneField(User, verbose_name='Untuk Pengguna')
    address = models.TextField(null=True, blank=True, verbose_name='Alamat')
    birthday = models.DateField('Tanggal Lahir', null=True)
    gender = models.CharField('Kelamin', max_length=1, choices=GENDER_CHOICES, default='l')
    phone = models.CharField('Telepon', max_length=20)
    photo = models.ImageField('Foto Profil', null=True, blank=True)
    
    def __unicode__(self):
        return self.user.first_name+" "+self.user.last_name
    
    def __str__(self):  # __unicode__ on Python 2
        return self.user.first_name+" "+self.user.last_name

    class Meta:
        verbose_name = "Anggota"
        verbose_name_plural = "Data Anggota"
        


class CareGiver(Member):
    class Meta:
        verbose_name = 'Perawat'
        verbose_name_plural = 'Data Perawat'


class Partner(Member):
    TYPE_CHOICES = (('rs', 'Rumah Sakit'), ('pj', 'Panti Jompo'),
                    ('km', 'Kelompok Minat'))

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField('Deskripsi', null=True, blank=True)
    type = models.CharField('Golongan Institusi', max_length=2, choices=TYPE_CHOICES, default='pj')


class Elder(Member):
    code = models.CharField('Kode Orang Tua', max_length=8, blank=False, null=False)
    cared_by = models.ManyToManyField(CareGiver, through='CareGiving', verbose_name='Dirawat oleh')

    class Meta:
        verbose_name = 'Orang Tua'
        verbose_name_plural = 'Data Orang Tua'

    @staticmethod
    def get_cared_elder(user):
        return Elder.objects.filter(cared_by__in=[user])
        
    def get_last_activity(self):
        reverse=self.tracker_set.order_by('-id')
        if reverse:
            return self.tracker_set.order_by('-id')[0]
        else:
            return None

    # def get_kondisi(self):
    #     return self.dailycondition_set
    #
    # def get_kondisi_terakhir(self):
    #     return self.dailycondition_set.latest('id')
    #
    # def count_perawat(self):
    #     return self.cared_by.count()
    #
    # def get_riwayat_penyakit(self):
    #     return self.diseasehist_set
    #
    # def get_perawatan_medis(self):
    #     return self.medicaltreatmenthist_set
    #
    # def get_note(self):
    #     return self.note_set
    #
    # def __unicode__(self):
    #     return self.user.username
    #
    # def __str__(self):  # __unicode__ on Python 2
    #     return self.user.username


class CareGiving(TimeStampedModel):
    caregiver = models.ForeignKey(CareGiver, null=True, verbose_name='Perawat')
    elder = models.ForeignKey(Elder, null=True, verbose_name='Orang Tua')

    class Meta:
        verbose_name = 'Perawatan'
        verbose_name_plural = 'Data Perawatan'


class AdminInvitation(TimeStampedModel, StatusModel):
    STATUS = Choices(('1', 'sent'), ('2', 'accepted'), ('3', 'rejected'))
    user = models.ForeignKey(User, verbose_name='Pemanggil')
    email_to_invite = models.CharField(max_length=45, verbose_name='Email yang akan dipanggil')

    class Meta:
        verbose_name = 'Pemanggilan Admin'
        verbose_name_plural = 'Data Pemanggilan Admin'
