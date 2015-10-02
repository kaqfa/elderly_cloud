# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('member', '0003_auto_20150929_1449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admininvitation',
            options={'verbose_name': 'Pemanggilan Admin', 'verbose_name_plural': 'Data Pemanggilan Admin'},
        ),
        migrations.AlterModelOptions(
            name='caregiver',
            options={'verbose_name': 'Perawat', 'verbose_name_plural': 'Data Perawat'},
        ),
        migrations.AlterModelOptions(
            name='caregiving',
            options={'verbose_name': 'Perawatan', 'verbose_name_plural': 'Data Perawatan'},
        ),
        migrations.AlterModelOptions(
            name='elder',
            options={'verbose_name': 'Orang Tua', 'verbose_name_plural': 'Data Orang Tua'},
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': 'Anggota', 'verbose_name_plural': 'Data Anggota'},
        ),
        migrations.AlterField(
            model_name='admininvitation',
            name='email_to_invite',
            field=models.CharField(max_length=45, verbose_name=b'Email yang akan dipanggil'),
        ),
        migrations.AlterField(
            model_name='admininvitation',
            name='user',
            field=models.ForeignKey(verbose_name=b'Pemanggil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='caregiving',
            name='caregiver',
            field=models.ForeignKey(verbose_name=b'Perawat', to='member.CareGiver', null=True),
        ),
        migrations.AlterField(
            model_name='caregiving',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Orang Tua', to='member.Elder', null=True),
        ),
        migrations.AlterField(
            model_name='elder',
            name='cared_by',
            field=models.ManyToManyField(to='member.CareGiver', verbose_name=b'Dirawat oleh',
                                         through='member.CareGiving'),
        ),
        migrations.AlterField(
            model_name='elder',
            name='code',
            field=models.CharField(max_length=8, verbose_name=b'Kode Orang Tua'),
        ),
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(null=True, verbose_name=b'Alamat', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, verbose_name=b'Tanggal Lahir'),
        ),
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(max_length=1, verbose_name=b'Kelamin'),
        ),
        migrations.AlterField(
            model_name='member',
            name='phone',
            field=models.CharField(max_length=20, verbose_name=b'Telepon'),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Foto Profil', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='user',
            field=models.OneToOneField(verbose_name=b'Untuk Pengguna', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='partner',
            name='description',
            field=models.TextField(null=True, verbose_name=b'Deskripsi', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(default=b'pj', max_length=2, verbose_name=b'Golongan Institusi',
                                   choices=[(b'rs', b'Rumah Sakit'), (b'pj', b'Panti Jompo'),
                                            (b'km', b'Kelompok Minat')]),
        ),
    ]
