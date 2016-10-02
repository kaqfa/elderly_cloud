# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20161003_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='condition',
            field=models.CharField(verbose_name='Kondisi', choices=[('ba', 'baik'), ('bi', 'kangen'), ('tb', 'panik'), ('sk', 'sakit kepala'), ('sl', 'sakit leher'), ('sdl', 'sakit dada kiri'), ('sdr', 'sakit dada kanan'), ('sal', 'sakit lengan atas kiri'), ('sar', 'sakit lengan atas kanan'), ('sll', 'sakit lengan kiri'), ('slr', 'sakit lengan kanan'), ('sp', 'sakit perut'), ('spl', 'sakit paha kiri'), ('spr', 'sakit paha kanan'), ('sbl', 'sakit betis kiri'), ('sbr', 'sakit betis kanan'), ('stl', 'sakit telapak kaki kiri'), ('str', 'sakit telapak kaki kanan'), ('ltl', 'sakit lutut kiri'), ('ltr', 'sakit lutut kanan')], default='ba', max_length=3),
        ),
    ]
