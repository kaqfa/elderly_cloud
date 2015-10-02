# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('tracker', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='elder',
            field=models.ForeignKey(to='member.Elder'),
        ),
    ]
