# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20151001_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.TextField(verbose_name='Pesan Notifikasi'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='invoked_on',
            field=models.DateTimeField(verbose_name='Dijalankan Pada', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(verbose_name='Tingkat Kepentingan', choices=[('1', 'info'), ('2', 'warning'), ('3', 'emergency')], max_length=1, default='1'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='receiver',
            field=models.ForeignKey(verbose_name='Kepada', related_name='notif_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recurring',
            field=models.CharField(verbose_name='Diulang Tiap', choices=[('1', 'sekali'), ('2', 'harian'), ('3', 'mingguan'), ('4', 'bulanan'), ('5', 'weekday'), ('6', 'weekend')], max_length=1, default='1'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='responded',
            field=models.ManyToManyField(through='notification.ResponseNotification', verbose_name='Direspon oleh', to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(verbose_name='Pengirim', related_name='notif_sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='title',
            field=models.CharField(verbose_name='Judul Notifikasi', max_length=45),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='content',
            field=models.TextField(verbose_name='Pesan Notifikasi'),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='level',
            field=models.CharField(verbose_name='Tingkat Kepentingan', choices=[('1', 'info'), ('2', 'warning'), ('3', 'emergency')], max_length=1, default='1'),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='title',
            field=models.CharField(verbose_name='Judul Notifikasi', max_length=45),
        ),
        migrations.AlterField(
            model_name='responsenotification',
            name='notification_id',
            field=models.ForeignKey(verbose_name='Untuk Notifikasi', to='notification.Notification'),
        ),
        migrations.AlterField(
            model_name='responsenotification',
            name='user_id',
            field=models.ForeignKey(verbose_name='Yang merespon', to=settings.AUTH_USER_MODEL),
        ),
    ]
