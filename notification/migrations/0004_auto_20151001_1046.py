# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('notification', '0003_auto_20151001_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(default=b'1s', max_length=1, verbose_name=b'Tingkat Kepentingan',
                                   choices=[(b'1', b'info'), (b'2', b'warning'), (b'3', b'emergency')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recurring',
            field=models.CharField(default=b'1', max_length=1, verbose_name=b'Diulang Tiap',
                                   choices=[(b'1', b'sekali'), (b'2', b'harian'), (b'3', b'mingguan'),
                                            (b'4', b'bulanan'), (b'5', b'weekday'), (b'6', b'weekend')]),
        ),
    ]
