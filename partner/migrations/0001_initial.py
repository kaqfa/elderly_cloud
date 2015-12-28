# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20151228_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'r', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'r', b'Rencana'), (b's', b'Selesai'), (b'g', b'Gagal')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('duedate', models.DateField(null=True, verbose_name=b'Tanggal', blank=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'Nama Kegiatan')),
                ('description', models.TextField(null=True, verbose_name=b'Deskripsi Kegiatan', blank=True)),
                ('owner', models.ForeignKey(to='member.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'k', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'k', b'Kosong'), (b't', b'Terpakai'), (b'r', b'Rusak'), (b'm', b'Maintenance')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('code', models.CharField(max_length=10, verbose_name=b'Kode')),
                ('name', models.CharField(max_length=50, verbose_name=b'Nama Kamar')),
                ('description', models.TextField(null=True, verbose_name=b'Deskripsi', blank=True)),
                ('owner', models.ForeignKey(to='member.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('name', models.CharField(max_length=10, verbose_name=b'Nama Kelas')),
                ('description', models.TextField(null=True, verbose_name=b'Deskripsi/Fasilitas', blank=True)),
                ('owner', models.ForeignKey(to='member.Partner')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='roomclass',
            field=models.ForeignKey(verbose_name=b'Kelas', to='partner.RoomClass'),
        ),
    ]
