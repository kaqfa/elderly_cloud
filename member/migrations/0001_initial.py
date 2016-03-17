# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInvitation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(no_check_for_status=True, choices=[('1', 'sent'), ('2', 'accepted'), ('3', 'rejected')], default='1', verbose_name='status', max_length=100)),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('email_to_invite', models.CharField(max_length=45, verbose_name='Email yang akan dipanggil')),
                ('user', models.ForeignKey(verbose_name='Pemanggil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data Pemanggilan Admin',
                'verbose_name': 'Pemanggilan Admin',
            },
        ),
        migrations.CreateModel(
            name='CareGiver',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('address', models.TextField(null=True, blank=True, verbose_name='Alamat')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Tanggal Lahir')),
                ('gender', models.CharField(choices=[('l', 'laki-laki'), ('p', 'perempuan')], default='l', verbose_name='Kelamin', max_length=1)),
                ('phone', models.CharField(max_length=20, default='', verbose_name='Telepon')),
                ('photo', models.ImageField(null=True, blank=True, upload_to='', verbose_name='Foto Profil')),
                ('user', models.OneToOneField(verbose_name='Untuk Pengguna', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data Perawat',
                'verbose_name': 'Perawat',
            },
        ),
        migrations.CreateModel(
            name='CareGiving',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('caregiver', models.ForeignKey(verbose_name='Perawat', null=True, to='member.CareGiver')),
            ],
            options={
                'verbose_name_plural': 'Data Perawatan',
                'verbose_name': 'Perawatan',
            },
        ),
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('address', models.TextField(null=True, blank=True, verbose_name='Alamat')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Tanggal Lahir')),
                ('gender', models.CharField(choices=[('l', 'laki-laki'), ('p', 'perempuan')], default='l', verbose_name='Kelamin', max_length=1)),
                ('phone', models.CharField(null=True, max_length=20, blank=True, verbose_name='Telepon')),
                ('photo', models.ImageField(null=True, blank=True, upload_to='', verbose_name='Foto Profil')),
                ('code', models.CharField(max_length=8, verbose_name='Kode Orang Tua')),
                ('cared_by', models.ManyToManyField(through='member.CareGiving', to='member.CareGiver', verbose_name='Dirawat oleh')),
                ('user', models.OneToOneField(verbose_name='Untuk Pengguna', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Data Orang Tua',
                'verbose_name': 'Orang Tua',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('address', models.TextField(null=True, blank=True, verbose_name='Alamat')),
                ('birthday', models.DateField(null=True, blank=True, verbose_name='Tanggal Lahir')),
                ('gender', models.CharField(choices=[('l', 'laki-laki'), ('p', 'perempuan')], default='l', verbose_name='Kelamin', max_length=1)),
                ('phone', models.CharField(null=True, max_length=20, blank=True, verbose_name='Telepon')),
                ('photo', models.ImageField(null=True, blank=True, upload_to='', verbose_name='Foto Profil')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592')),
                ('description', models.TextField(null=True, blank=True, verbose_name='Deskripsi')),
                ('type', models.CharField(choices=[('rs', 'Rumah Sakit'), ('pj', 'Panti Jompo'), ('km', 'Komunitas')], default='pj', verbose_name='Golongan Institusi', max_length=2)),
                ('user', models.OneToOneField(verbose_name='Untuk Pengguna', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='caregiving',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', null=True, to='member.Elder'),
        ),
    ]
