# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('feedback', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Umpan Balik', 'verbose_name_plural': 'Data Umpan Balik'},
        ),
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Respon Umpan Balik', 'verbose_name_plural': 'Respon Umpan Balik'},
        ),
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(default=b'', verbose_name=b'Isi Umpan Balik'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='owner',
            field=models.ForeignKey(verbose_name=b'Pengirim', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(default=b'', max_length=120, verbose_name=b'Judul Umpan Balik'),
        ),
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(default=b'', verbose_name=b'Isi Respon'),
        ),
        migrations.AlterField(
            model_name='response',
            name='feedback',
            field=models.ForeignKey(verbose_name=b'Untuk Umpan Balik', to='feedback.Feedback'),
        ),
        migrations.AlterField(
            model_name='response',
            name='owner',
            field=models.ForeignKey(verbose_name=b'Penulis', to=settings.AUTH_USER_MODEL),
        ),
    ]
