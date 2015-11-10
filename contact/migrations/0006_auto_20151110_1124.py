# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20151001_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='added_by',
            field=models.ForeignKey(verbose_name='Ditambahkan oleh', to='member.CareGiver'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(verbose_name='Alamat Kontak', null=True, max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='elder',
            field=models.ForeignKey(verbose_name='Kontak untuk', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(verbose_name='Email Kontak', null=True, max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(verbose_name='Nama Kontak', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(verbose_name='Telepon Kontak', max_length=25, default=''),
        ),
    ]
