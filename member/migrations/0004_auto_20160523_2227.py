# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20160523_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elder',
            name='phone',
            field=models.CharField(verbose_name='Telepon', max_length=20, unique=True, default='000-000-000'),
        ),
    ]
