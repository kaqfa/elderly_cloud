# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20151001_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Isi Komentar'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(verbose_name='Penulis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(verbose_name='Untuk Posting', to='info.Posting'),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='address',
            field=models.CharField(verbose_name='Alamat', max_length=45),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='category',
            field=models.CharField(verbose_name='Kategori', max_length=45),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='name',
            field=models.CharField(verbose_name='Nama Lokasi', max_length=45),
        ),
        migrations.AlterField(
            model_name='posting',
            name='category',
            field=models.CharField(verbose_name='Kategori', max_length=45),
        ),
        migrations.AlterField(
            model_name='posting',
            name='content',
            field=models.TextField(verbose_name='Isi Posting'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(verbose_name='Penulis', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posting',
            name='title',
            field=models.CharField(verbose_name='Judul Posting', max_length=45),
        ),
    ]
