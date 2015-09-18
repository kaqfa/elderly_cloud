# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0002_note_daily_condition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasehist',
            old_name='disease',
            new_name='name',
        ),
        migrations.AddField(
            model_name='dailycondition',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
