# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ('contact', '0002_contact_elder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=model_utils.fields.StatusField(default='1', no_check_for_status=True, verbose_name='status',
                                                 max_length=100, choices=[(0, 'dummy')]),
        ),
    ]
