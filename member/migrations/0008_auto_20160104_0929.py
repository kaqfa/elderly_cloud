# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20151228_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='type',
            field=models.CharField(max_length=2, default='pj', choices=[('rs', 'Rumah Sakit'), ('pj', 'Panti Jompo'), ('km', 'Komunitas')], verbose_name='Golongan Institusi'),
        ),
    ]
