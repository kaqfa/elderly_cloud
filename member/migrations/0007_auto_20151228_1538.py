# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20151110_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partner',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='partner',
            name='longitude',
        ),
        migrations.AddField(
            model_name='partner',
            name='location',
            field=location_field.models.plain.PlainLocationField(default=b'-6.889836,109.674592', max_length=63),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(default=b'pj', max_length=2, verbose_name=b'Golongan Institusi', choices=[(b'rs', b'Rumah Sakit'), (b'pj', b'Panti Jompo'), (b'km', b'Komunitas')]),
        ),
    ]
