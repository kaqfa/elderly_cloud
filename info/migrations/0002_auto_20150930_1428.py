# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Komentar', 'verbose_name_plural': 'Data Komentar'},
        ),
        migrations.AlterModelOptions(
            name='posting',
            options={'verbose_name': 'Posting Informasi', 'verbose_name_plural': 'Posting Informasi'},
        ),
        migrations.RenameField(
            model_name='pointofinterest',
            old_name='lattitude',
            new_name='latitude',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name=b'Isi Komentar'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(verbose_name=b'Penulis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(verbose_name=b'Untuk Posting', to='info.Posting'),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='address',
            field=models.CharField(max_length=45, verbose_name=b'Alamat'),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='category',
            field=models.CharField(max_length=45, verbose_name=b'Kategori'),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='name',
            field=models.CharField(max_length=45, verbose_name=b'Nama Lokasi'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='category',
            field=models.CharField(max_length=45, verbose_name=b'Kategori'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='content',
            field=models.TextField(verbose_name=b'Isi Posting'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(verbose_name=b'Penulis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posting',
            name='title',
            field=models.CharField(max_length=45, verbose_name=b'Judul Posting'),
        ),
    ]
