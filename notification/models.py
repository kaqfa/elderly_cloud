from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices

from member.models import Elder


class NotificationTemplate(models.Model):
    LEVEL_CHOICES = (('1', 'info'), ('2', 'warning'), ('3', 'emergency'))
    title = models.CharField('Judul Notifikasi', max_length=45)
    content = models.TextField('Pesan Notifikasi')
    level = models.CharField('Tingkat Kepentingan', max_length=1, choices=LEVEL_CHOICES, default='1')

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Template'


class Notification(TimeStampedModel, StatusModel):
    STATUS = Choices(('s', 'sent'), ('r', 'responded'))
    LEVEL_CHOICES = (('1', 'info'), ('2', 'warning'), ('3', 'emergency'))
    RECUR_CHOICES = (('1', 'sekali'), ('2', 'harian'), ('3', 'mingguan'),
                     ('4', 'bulanan'), ('5', 'weekday'), ('6', 'weekend'))

    title = models.CharField('Judul Notifikasi', max_length=45)
    content = models.TextField('Pesan Notifikasi')
    invoked_on = models.DateTimeField('Dijalankan Pada', null=True, blank=True)
    recurring = models.CharField('Diulang Tiap', max_length=1, choices=RECUR_CHOICES,
                                 default='1')
    level = models.CharField('Tingkat Kepentingan', max_length=1, choices=LEVEL_CHOICES,
                             default='1s')
    sender = models.ForeignKey(User, related_name='notif_sender', verbose_name='Pengirim')
    receiver = models.ForeignKey(User, related_name='notif_receiver', verbose_name='Kepada')
    responded = models.ManyToManyField(User, blank=True, through='ResponseNotification',
                                       verbose_name='Direspon oleh')

    class Meta:
        verbose_name = 'Notifikasi'
        verbose_name_plural = 'Data Notifikasi'


class ResponseNotification(TimeStampedModel):
    user_id = models.ForeignKey(User, verbose_name='Yang merespon')
    notification_id = models.ForeignKey(Notification, verbose_name='Untuk Notifikasi')
