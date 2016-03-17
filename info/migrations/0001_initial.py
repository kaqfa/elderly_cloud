# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='Isi Komentar')),
                ('owner', models.ForeignKey(verbose_name='Penulis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data Komentar',
                'verbose_name': 'Komentar',
            },
        ),
        migrations.CreateModel(
            name='PointOfInterest',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, verbose_name='Nama Lokasi')),
                ('category', models.CharField(max_length=45, verbose_name='Kategori')),
                ('address', models.CharField(max_length=45, verbose_name='Alamat')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592')),
            ],
            options={
                'verbose_name_plural': 'Data Lokasi Menarik',
                'verbose_name': 'Lokasi Menarik',
            },
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45, verbose_name='Judul Posting')),
                ('content', models.TextField(verbose_name='Isi Posting')),
                ('category', models.CharField(max_length=45, verbose_name='Kategori')),
                ('owner', models.ForeignKey(verbose_name='Penulis', default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Posting Informasi',
                'verbose_name': 'Posting Informasi',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='posting',
            field=models.ForeignKey(verbose_name='Untuk Posting', to='info.Posting'),
        ),
    ]
