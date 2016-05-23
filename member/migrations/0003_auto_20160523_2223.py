# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160507_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elder',
            name='code',
            field=models.CharField(max_length=20, verbose_name='Kode Orang Tua'),
        ),
        migrations.AlterField(
            model_name='elder',
            name='phone',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Telepon'),
        ),
    ]
