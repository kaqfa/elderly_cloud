# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('elder_profile', '0003_auto_20150930_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasehist',
            name='from_year',
            field=models.IntegerField(default=2015, verbose_name=b'Dari Tahun'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='to_year',
            field=models.IntegerField(default=2015, verbose_name=b'Hingga Tahun'),
        ),
    ]
