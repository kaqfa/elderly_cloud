from django.db import models
from member.models import Partner
from polymorphic import PolymorphicModel
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices


class RoomClass(TimeStampedModel):
    name = models.CharField('Nama Kelas', max_length=10)
    description = models.TextField('Deskripsi/Fasilitas', blank=True, null=True)
    owner = models.ForeignKey(Partner)


# room hanya untuk partner yang RS & panti
class Room(TimeStampedModel, StatusModel):
    STATUS = (('k','Kosong'), ('t','Terpakai'), ('r','Rusak'), ('m','Maintenance'))

    code = models.CharField('Kode', max_length=10)
    name = models.CharField('Nama Kamar', max_length=50)
    roomclass = models.ForeignKey(RoomClass, verbose_name = 'Kelas')
    description = models.TextField('Deskripsi', blank=True, null=True)
    owner = models.ForeignKey(Partner)


# Agenda hanya untuk partner komunitas
class Agenda(TimeStampedModel, StatusModel):
    STATUS = (('r','Rencana'),('s','Selesai'),('g','Gagal'))

    duedate = models.DateField('Tanggal', blank=True, null=True)
    name = models.CharField('Nama Kegiatan', max_length=200)
    description = models.TextField('Deskripsi Kegiatan', blank=True, null=True)
    owner = models.ForeignKey(Partner)
