# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20151110_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pointofinterest',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='pointofinterest',
            name='longitude',
        ),
        migrations.AddField(
            model_name='pointofinterest',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592'),
        ),
    ]
