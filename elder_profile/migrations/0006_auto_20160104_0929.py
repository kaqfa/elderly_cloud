# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0005_auto_20151110_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasehist',
            name='from_year',
            field=models.IntegerField(default=2016, verbose_name='Dari Tahun'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='to_year',
            field=models.IntegerField(default=2016, verbose_name='Hingga Tahun'),
        ),
    ]
