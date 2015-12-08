# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20151208_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='location',
            field=location_field.models.plain.PlainLocationField(default='-6.889836,109.674592', max_length=63),
        ),
    ]
