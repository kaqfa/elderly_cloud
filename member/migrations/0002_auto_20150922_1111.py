# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admininvitation',
            name='status',
            field=model_utils.fields.StatusField(default='1', no_check_for_status=True, verbose_name='status',
                                                 max_length=100, choices=[(0, 'dummy')]),
        ),
    ]
