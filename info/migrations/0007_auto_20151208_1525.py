# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20151208_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(verbose_name=b'Penulis', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
