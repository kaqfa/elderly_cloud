# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20151001_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Orang Tua', to='member.Elder'),
        ),
    ]
