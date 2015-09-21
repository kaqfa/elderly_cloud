# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b's', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b's', b'sent'), (b'r', b'responded')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('invoked_on', models.DateTimeField(null=True, blank=True)),
                ('recurring', models.CharField(max_length=1, choices=[(b'1', b'sekali'), (b'2', b'harian'), (b'3', b'mingguan'), (b'4', b'bulanan'), (b'5', b'weekday'), (b'6', b'weekend')])),
                ('level', models.CharField(max_length=1, choices=[(b'1', b'info'), (b'2', b'warning'), (b'3', b'emergency')])),
                ('receiver', models.ForeignKey(related_name='notif_receiver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('level', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'info'), (b'2', b'warning'), (b'3', b'emergency')])),
            ],
        ),
        migrations.CreateModel(
            name='ResponseNotification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('notification_id', models.ForeignKey(to='notification.Notification')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='notification',
            name='responded',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='notification.ResponseNotification', blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender',
            field=models.ForeignKey(related_name='notif_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]
