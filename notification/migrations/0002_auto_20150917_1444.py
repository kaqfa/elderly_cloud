# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emergencycall',
            old_name='emergancy_time',
            new_name='emergency_time',
        ),
        migrations.AlterField(
            model_name='emergencycall',
            name='responded_by',
            field=models.ManyToManyField(through='notification.ResponseEmergencyCall', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
