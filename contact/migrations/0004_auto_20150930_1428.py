# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0003_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Kontak', 'verbose_name_plural': 'Data Kontak'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='added_by',
            field=models.ForeignKey(verbose_name=b'Ditambahkan oleh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name=b'Alamat Kontak', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Kontak untuk', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Email Kontak', blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'Nama Kontak'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=b'', max_length=25, verbose_name=b'Telepon Kontak'),
        ),
    ]
