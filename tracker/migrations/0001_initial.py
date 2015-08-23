# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogTracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value1', models.IntegerField(default=0)),
                ('value2', models.IntegerField(default=0)),
                ('value3', models.IntegerField(default=0)),
                ('value4', models.IntegerField(default=0)),
                ('value5', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=45)),
                ('field1', models.CharField(max_length=45)),
                ('field2', models.CharField(max_length=45)),
                ('field3', models.CharField(max_length=45)),
                ('field4', models.CharField(max_length=45)),
                ('field5', models.CharField(max_length=45)),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='TrackerTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=45)),
                ('field1', models.CharField(max_length=45)),
                ('field2', models.CharField(max_length=45)),
                ('field3', models.CharField(max_length=45)),
                ('field4', models.CharField(max_length=45)),
                ('field5', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='logtracker',
            name='tracker',
            field=models.ForeignKey(to='tracker.Tracker'),
        ),
    ]
