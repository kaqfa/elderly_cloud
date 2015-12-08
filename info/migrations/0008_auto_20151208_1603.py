# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20151208_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(default=1, verbose_name=b'Penulis', to=settings.AUTH_USER_MODEL),
        ),
    ]
