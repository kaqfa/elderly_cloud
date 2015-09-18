# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elder',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='elder',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='elder',
            name='gender',
            field=models.CharField(max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='elder',
            name='name',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
