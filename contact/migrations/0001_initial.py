# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0002_auto_20150917_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(null=True, blank=True, max_length=200)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(null=True, blank=True, max_length=255)),
                ('status', models.CharField(max_length=1)),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
    ]
