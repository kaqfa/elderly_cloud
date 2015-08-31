# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='daily_condition',
            field=models.ForeignKey(blank=True, to='elder_profile.DailyCondition', null=True),
        ),
    ]
