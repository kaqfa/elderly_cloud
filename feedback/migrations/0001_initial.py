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
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created',
                 model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created',
                                                     editable=False)),
                ('modified',
                 model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified',
                                                          editable=False)),
                ('status', model_utils.fields.StatusField(default=b's', max_length=100, verbose_name='status',
                                                          no_check_for_status=True,
                                                          choices=[(b's', b'sent'), (b'r', b'responded'),
                                                                   (b'c', b'closed')])),
                ('status_changed',
                 model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed',
                                                 monitor='status')),
                ('title', models.CharField(default=b'', max_length=120)),
                ('content', models.TextField(default=b'')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(default=b'')),
                ('feedback', models.ForeignKey(to='feedback.Feedback')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
