# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20151002_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='condition',
            field=models.SmallIntegerField(verbose_name='Kondisi', choices=[(1, 'tidak baik'), (2, 'biasa'), (3, 'baik')], default=3),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='photo',
            field=models.ImageField(verbose_name='Gambar', upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='type',
            field=models.CharField(verbose_name='Jenis Penelusuran', choices=[('cd', 'daily condition'), ('hr', 'heart rate'), ('bg', 'blood glucose')], max_length=2, default='cd'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='value',
            field=models.SmallIntegerField(verbose_name='Nilai', default=0),
        ),
    ]
