from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices
from model_utils.models import TimeStampedModel, StatusModel


class Feedback(TimeStampedModel, StatusModel):
    STATUS = Choices(('s', 'sent'), ('r', 'responded'), ('c', 'closed'))
    owner = models.ForeignKey(User, verbose_name='Pengirim')
    title = models.CharField('Judul Umpan Balik', max_length=120, default='')
    content = models.TextField('Isi Umpan Balik', default='')

    class Meta:
        verbose_name = 'Umpan Balik'
        verbose_name_plural = 'Data Umpan Balik'


class Response(models.Model):
    owner = models.ForeignKey(User, verbose_name='Penulis')
    feedback = models.ForeignKey(Feedback, verbose_name='Untuk Umpan Balik')
    content = models.TextField('Isi Respon', default='')

    class Meta:
        verbose_name = 'Respon Umpan Balik'
        verbose_name_plural = 'Respon Umpan Balik'