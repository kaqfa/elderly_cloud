# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=model_utils.fields.StatusField(default='s', no_check_for_status=True, verbose_name='status', max_length=100, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='title',
            field=models.CharField(default='', max_length=120),
        ),
        migrations.AlterField(
            model_name='response',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
