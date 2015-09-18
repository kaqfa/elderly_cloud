# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='response',
            name='feedback',
            field=models.ForeignKey(to='feedback.Feedback'),
        ),
        migrations.AddField(
            model_name='response',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
