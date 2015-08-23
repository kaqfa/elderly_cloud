# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_to_invite', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=1)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Caregiving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=8)),
                ('name', models.CharField(default=b'', max_length=100)),
                ('cared_by', models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='member.Caregiving')),
            ],
        ),
        migrations.AddField(
            model_name='caregiving',
            name='elder',
            field=models.ForeignKey(to='member.Elder'),
        ),
        migrations.AddField(
            model_name='caregiving',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
