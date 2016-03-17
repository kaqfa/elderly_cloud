# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(editable=False, default=django.utils.timezone.now, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, default=django.utils.timezone.now, verbose_name='modified')),
                ('type', models.CharField(choices=[('dc', 'daily condition'), ('hr', 'heart rate'), ('bg', 'blood glucose')], default='dc', verbose_name='Jenis Penelusuran', max_length=2)),
                ('condition', models.CharField(choices=[('ba', 'baik'), ('bi', 'biasa'), ('tb', 'tidak baik'), ('sk', 'sakit kepala'), ('sl', 'sakit leher'), ('sdl', 'sakit dada kiri'), ('sdr', 'sakit dada kanan'), ('sll', 'sakit lengan kiri'), ('slr', 'sakit lengan kanan'), ('sp', 'sakit perut'), ('spl', 'sakit paha kiri'), ('spr', 'sakit paha kanan'), ('sbl', 'sakit betis kiri'), ('sbr', 'sakit betis kanan'), ('stl', 'sakit telapak kaki kiri'), ('str', 'sakit telapak kaki kanan')], default=3, verbose_name='Kondisi', max_length=3)),
                ('value', models.SmallIntegerField(default=0, verbose_name='Nilai')),
                ('photo', models.ImageField(null=True, blank=True, upload_to='', verbose_name='Gambar')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592')),
                ('elder', models.ForeignKey(verbose_name='Orang Tua', to='member.Elder')),
            ],
            options={
                'verbose_name_plural': 'Data Penelusuran',
                'verbose_name': 'Penelusuran',
            },
        ),
    ]
