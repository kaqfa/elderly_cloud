# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0004_auto_20150930_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='added_by',
            field=models.ForeignKey(verbose_name=b'Ditambahkan oleh', to='member.CareGiver'),
        ),
    ]
