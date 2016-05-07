# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='condition',
            field=models.CharField(max_length=3, verbose_name='Kondisi', default='ba', choices=[('ba', 'baik'), ('bi', 'biasa'), ('tb', 'tidak baik'), ('sk', 'sakit kepala'), ('sl', 'sakit leher'), ('sdl', 'sakit dada kiri'), ('sdr', 'sakit dada kanan'), ('sll', 'sakit lengan kiri'), ('slr', 'sakit lengan kanan'), ('sp', 'sakit perut'), ('spl', 'sakit paha kiri'), ('spr', 'sakit paha kanan'), ('sbl', 'sakit betis kiri'), ('sbr', 'sakit betis kanan'), ('stl', 'sakit telapak kaki kiri'), ('str', 'sakit telapak kaki kanan')]),
        ),
    ]
