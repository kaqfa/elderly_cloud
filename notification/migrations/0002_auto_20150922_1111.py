# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='level',
            field=models.CharField(max_length=1, choices=[('1', 'info'), ('2', 'warning'), ('3', 'emergency')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recurring',
            field=models.CharField(max_length=1,
                                   choices=[('1', 'sekali'), ('2', 'harian'), ('3', 'mingguan'), ('4', 'bulanan'),
                                            ('5', 'weekday'), ('6', 'weekend')]),
        ),
        migrations.AlterField(
            model_name='notification',
            name='status',
            field=model_utils.fields.StatusField(default='s', no_check_for_status=True, verbose_name='status',
                                                 max_length=100, choices=[(0, 'dummy')]),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='level',
            field=models.CharField(default='1', max_length=1,
                                   choices=[('1', 'info'), ('2', 'warning'), ('3', 'emergency')]),
        ),
    ]
