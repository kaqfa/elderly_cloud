# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20151001_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(default=b'l', max_length=1, verbose_name=b'Kelamin', choices=[(b'l', b'laki-laki'), (b'p', b'perempuan')]),
        ),
    ]
