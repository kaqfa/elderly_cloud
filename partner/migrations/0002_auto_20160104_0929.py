# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20160104_0929'),
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('owner', models.OneToOneField(primary_key=True, serialize=False, to='member.Partner')),
                ('num', models.PositiveIntegerField(verbose_name='Jumlah Ketersediaan Ruangan')),
            ],
        ),
        migrations.AlterField(
            model_name='agenda',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Deskripsi Kegiatan'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='duedate',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nama Kegiatan'),
        ),
        migrations.AlterField(
            model_name='agenda',
            name='status',
            field=model_utils.fields.StatusField(max_length=100, default='r', choices=[(0, 'dummy')], verbose_name='status', no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(max_length=10, verbose_name='Kode'),
        ),
        migrations.AlterField(
            model_name='room',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Deskripsi'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nama Kamar'),
        ),
        migrations.AlterField(
            model_name='room',
            name='roomclass',
            field=models.ForeignKey(verbose_name='Kelas', to='partner.RoomClass'),
        ),
        migrations.AlterField(
            model_name='room',
            name='status',
            field=model_utils.fields.StatusField(max_length=100, default='k', choices=[(0, 'dummy')], verbose_name='status', no_check_for_status=True),
        ),
        migrations.AlterField(
            model_name='roomclass',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Deskripsi/Fasilitas'),
        ),
        migrations.AlterField(
            model_name='roomclass',
            name='name',
            field=models.CharField(max_length=10, verbose_name='Nama Kelas'),
        ),
    ]
