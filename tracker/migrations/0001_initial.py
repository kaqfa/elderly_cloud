# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('condition', models.SmallIntegerField(default=3, choices=[(1, b'tidak baik'), (2, b'biasa'), (3, b'baik')])),
                ('photo', models.ImageField(null=True, upload_to=b'')),
                ('type', models.CharField(default=b'cd', max_length=2, choices=[(b'cd', b'daily condition'), (b'hr', b'heart rate'), (b'bg', b'blood glucose')])),
                ('value', models.SmallIntegerField(default=0)),
                ('elder', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
