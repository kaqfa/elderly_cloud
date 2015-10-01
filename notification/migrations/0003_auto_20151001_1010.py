# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Notifikasi', 'verbose_name_plural': 'Data Notifikasi'},
        ),
        migrations.AlterModelOptions(
            name='notificationtemplate',
            options={'verbose_name': 'Template', 'verbose_name_plural': 'Template'},
        ),
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(verbose_name=b'Pesan Notifikasi'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='invoked_on',
            field=models.DateTimeField(null=True, verbose_name=b'Dijalankan Pada', blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(max_length=1, verbose_name=b'Tingkat Kepentingan', choices=[(b'1', b'info'), (b'2', b'warning'), (b'3', b'emergency')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(related_name='notif_receiver', verbose_name=b'Kepada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recurring',
            field=models.CharField(max_length=1, verbose_name=b'Diulang Tiap', choices=[(b'1', b'sekali'), (b'2', b'harian'), (b'3', b'mingguan'), (b'4', b'bulanan'), (b'5', b'weekday'), (b'6', b'weekend')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='responded',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Direspon oleh', through='notification.ResponseNotification', blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(related_name='notif_sender', verbose_name=b'Pengirim', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(max_length=45, verbose_name=b'Judul Notifikasi'),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='content',
            field=models.TextField(verbose_name=b'Pesan Notifikasi'),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='level',
            field=models.CharField(default=b'1', max_length=1, verbose_name=b'Tingkat Kepentingan', choices=[(b'1', b'info'), (b'2', b'warning'), (b'3', b'emergency')]),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='title',
            field=models.CharField(max_length=45, verbose_name=b'Judul Notifikasi'),
        ),
        migrations.AlterField(
            model_name='responsenotification',
            name='notification_id',
            field=models.ForeignKey(verbose_name=b'Untuk Notifikasi', to='notification.Notification'),
        ),
        migrations.AlterField(
            model_name='responsenotification',
            name='user_id',
            field=models.ForeignKey(verbose_name=b'Yang merespon', to=settings.AUTH_USER_MODEL),
        ),
    ]
