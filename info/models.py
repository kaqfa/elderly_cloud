from django.db import models
from django.contrib.auth.models import User


class Posting(models.Model):
    owner = models.ForeignKey(User, verbose_name='Penulis')
    title = models.CharField('Judul Posting', max_length=45)
    content = models.TextField('Isi Posting')
    category = models.CharField('Kategori', max_length=45)

    class Meta:
        verbose_name = 'Posting Informasi'
        verbose_name_plural = 'Posting Informasi'

    @staticmethod
    def get_latest_post():
        return Posting.objects.order_by('-id')[:10]


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
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
