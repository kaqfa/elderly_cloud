# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20160507_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elder',
            name='phone',
            field=models.CharField(verbose_name='Telepon', default='', unique=True, max_length=20),
        ),
    ]
