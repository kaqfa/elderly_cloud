# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Artikel', 'verbose_name': 'Artikel'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategori', 'verbose_name': 'Kategori'},
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(default=None, verbose_name='Berita'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 20, 16, 45, 31, 918822), verbose_name='Tanggal Berita'),
            preserve_default=False,
        ),
    ]
