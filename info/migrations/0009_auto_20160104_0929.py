# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_auto_20151208_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='owner',
            field=models.ForeignKey(default=1, verbose_name='Penulis', to=settings.AUTH_USER_MODEL),
        ),
    ]
