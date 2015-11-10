# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20151001_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(verbose_name='Isi Umpan Balik', default=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='owner',
            field=models.ForeignKey(verbose_name='Pengirim', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(verbose_name='Judul Umpan Balik', max_length=120, default=''),
        ),
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(verbose_name='Isi Respon', default=''),
        ),
        migrations.AlterField(
            model_name='response',
            name='feedback',
            field=models.ForeignKey(verbose_name='Untuk Umpan Balik', to='feedback.Feedback'),
        ),
        migrations.AlterField(
            model_name='response',
            name='owner',
            field=models.ForeignKey(verbose_name='Penulis', to=settings.AUTH_USER_MODEL),
        ),
    ]
