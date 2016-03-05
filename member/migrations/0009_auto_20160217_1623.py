# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20160104_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='birthday',
            field=models.DateField(null=True, verbose_name='Tanggal Lahir', blank=True),
        ),
    ]
