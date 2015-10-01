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
            name='condition',
            field=models.SmallIntegerField(default=3, choices=[(1, 'tidak baik'), (2, 'biasa'), (3, 'baik')]),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='photo',
            field=models.ImageField(upload_to='', null=True),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='type',
            field=models.CharField(default='cd', max_length=2,
                                   choices=[('cd', 'daily condition'), ('hr', 'heart rate'), ('bg', 'blood glucose')]),
        ),
    ]
