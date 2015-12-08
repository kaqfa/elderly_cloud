# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20151110_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='photo',
            field=models.ImageField(upload_to='', null=True, blank=True, verbose_name='Gambar'),
        ),
    ]
