# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20151001_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininvitation',
            name='email_to_invite',
            field=models.CharField(verbose_name='Email yang akan dipanggil', max_length=45),
        ),
        migrations.AlterField(
            model_name='admininvitation',
            name='user',
            field=models.ForeignKey(verbose_name='Pemanggil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='caregiving',
            name='caregiver',
            field=models.ForeignKey(verbose_name='Perawat', null=True, to='member.CareGiver'),
        ),
        migrations.AlterField(
            model_name='caregiving',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', null=True, to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='elder',
            name='cared_by',
            field=models.ManyToManyField(through='member.CareGiving', verbose_name='Dirawat oleh', to='member.CareGiver'),
        ),
        migrations.AlterField(
            model_name='elder',
            name='code',
            field=models.CharField(verbose_name='Kode Orang Tua', max_length=8),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(verbose_name='Alamat', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(verbose_name='Tanggal Lahir', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(verbose_name='Kelamin', choices=[('l', 'laki-laki'), ('p', 'perempuan')], max_length=1, default='l'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(verbose_name='Telepon', max_length=20),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(verbose_name='Foto Profil', upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(verbose_name='Untuk Pengguna', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(verbose_name='Deskripsi', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(verbose_name='Golongan Institusi', choices=[('rs', 'Rumah Sakit'), ('pj', 'Panti Jompo'), ('km', 'Kelompok Minat')], max_length=2, default='pj'),
        ),
    ]
