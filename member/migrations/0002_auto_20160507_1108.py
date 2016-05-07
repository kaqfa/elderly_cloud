# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elder',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Telepon', unique=True, null=True, blank=True),
        ),
    ]
