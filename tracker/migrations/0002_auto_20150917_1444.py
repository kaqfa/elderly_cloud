# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='name',
            field=models.CharField(max_length=45, default=''),
        ),
        migrations.AlterField(
            model_name='trackertemplate',
            name='name',
            field=models.CharField(max_length=45, default=''),
        ),
    ]
