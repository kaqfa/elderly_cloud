# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='elder',
            field=models.ForeignKey(to='member.Elder'),
        ),
    ]
