# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasehist',
            name='elder',
            field=models.ForeignKey(to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='status',
            field=model_utils.fields.StatusField(default='1', no_check_for_status=True, verbose_name='status', max_length=100, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='elder',
            field=models.ForeignKey(to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='status',
            field=model_utils.fields.StatusField(default='1', no_check_for_status=True, verbose_name='status', max_length=100, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='note',
            name='sharable',
            field=models.CharField(default='1', max_length=1, choices=[('1', 'yes'), ('0', 'no')]),
        ),
    ]
