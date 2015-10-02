# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('member', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='latitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='longitude',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='type',
            field=models.CharField(default=b'pj', max_length=2,
                                   choices=[(b'rs', b'Rumah Sakit'), (b'pj', b'Panti Jompo'),
                                            (b'km', b'Kelompok Minat')]),
        ),
    ]
