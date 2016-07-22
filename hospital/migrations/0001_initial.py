# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Nama', max_length=200)),
                ('address', models.TextField(verbose_name='Alamat', blank=True, null=True)),
                ('phone', models.CharField(verbose_name='Telepon', max_length=20, default='')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63, default='-6.889836,109.674592')),
            ],
            options={
                'verbose_name': 'Rumah Sakit',
                'verbose_name_plural': 'Rumah Sakit',
            },
        ),
    ]
