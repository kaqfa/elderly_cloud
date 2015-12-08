from django.db import models
from django.contrib.auth.models import User
from location_field.models.plain import PlainLocationField


class Posting(models.Model):
    owner = models.ForeignKey(User, verbose_name='Penulis', default=1)
    title = models.CharField('Judul Posting', max_length=45)
    content = models.TextField('Isi Posting')
    category = models.CharField('Kategori', max_length=45)

    class Meta:
        verbose_name = 'Posting Informasi'
        verbose_name_plural = 'Posting Informasi'

    @staticmethod
    def get_latest_post():
        return Posting.objects.all().order_by('-id')[:5]


class Comment(models.Model):
    owner = models.ForeignKey(User, verbose_name='Penulis')
    posting = models.ForeignKey(Posting, verbose_name='Untuk Posting')
    content = models.TextField('Isi Komentar')

    class Meta:
        verbose_name = 'Komentar'
        verbose_name_plural = 'Data Komentar'


class PointOfInterest(models.Model):
    name = models.CharField('Nama Lokasi', max_length=45)
    category = models.CharField('Kategori', max_length=45)
    address = models.CharField('Alamat', max_length=45)
    location = PlainLocationField(based_fields=[address], zoom=7, default='-6.889836,109.674592')

    class Meta:
        verbose_name = 'Lokasi Menarik'
        verbose_name_plural = 'Data Lokasi Menarik'
