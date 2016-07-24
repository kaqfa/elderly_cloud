# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160720_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(verbose_name='Ditulis Oleh', to=settings.AUTH_USER_MODEL),
        ),
    ]
