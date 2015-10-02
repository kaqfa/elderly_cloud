# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('info', '0002_auto_20150930_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pointofinterest',
            options={'verbose_name': 'Lokasi Menarik', 'verbose_name_plural': 'Data Lokasi Menarik'},
        ),
    ]
