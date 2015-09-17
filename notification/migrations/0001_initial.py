# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emergancy_time', models.DateTimeField()),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResponseEmergencyCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emergency_call_id', models.ForeignKey(to='notification.EmergencyCall')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='emergencycall',
            name='responded_by',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True,
                                         through='notification.ResponseEmergencyCall', blank=True),
        ),
    ]
