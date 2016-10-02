# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160523_2223'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackCondition',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('tracker.tracker',),
        ),
        migrations.CreateModel(
            name='TrackPanic',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('tracker.tracker',),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='condition',
            field=models.CharField(default='ba', max_length=3, verbose_name='Kondisi', choices=[('ba', 'baik'), ('bi', 'kangen'), ('tb', 'panik'), ('sk', 'sakit kepala'), ('sl', 'sakit leher'), ('sdl', 'sakit dada kiri'), ('sdr', 'sakit dada kanan'), ('sal', 'sakit lengan atas kiri'), ('sar', 'sakit lengan atas kanan'), ('sll', 'sakit lengan kiri'), ('slr', 'sakit lengan kanan'), ('sp', 'sakit perut'), ('spl', 'sakit paha kiri'), ('spr', 'sakit paha kanan'), ('sbl', 'sakit betis kiri'), ('sbr', 'sakit betis kanan'), ('stl', 'sakit telapak kaki kiri'), ('str', 'sakit telapak kaki kanan'), ('sltl', 'sakit lutut kiri'), ('sltr', 'sakit lutut kanan')]),
        ),
    ]
