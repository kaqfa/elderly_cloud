# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_invitation',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email_to_invite', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Caregiving',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Daily_condition',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('condition', models.CharField(max_length=45)),
                ('time_record', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Disease_hist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('disease', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=45)),
                ('name', models.CharField(default='', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Emergency_call',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('emergancy_time', models.DateTimeField()),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('feedback', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Log_tracker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('value1', models.IntegerField(default=0)),
                ('value2', models.IntegerField(default=0)),
                ('value3', models.IntegerField(default=0)),
                ('value4', models.IntegerField(default=0)),
                ('value5', models.IntegerField(default=0)),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Medical_treatment_hist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('treatment', models.TextField()),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('dosage', models.CharField(max_length=45)),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Notif_template',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('notif', models.CharField(max_length=45)),
                ('elder_id', models.ForeignKey(to='backend.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Point_of_interest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('category', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('lattitude', models.CharField(max_length=45)),
                ('longitude', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Respond_emergency_call',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('emergency_call_id', models.ForeignKey(to='backend.Emergency_call')),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
                ('field1', models.CharField(max_length=45)),
                ('field2', models.CharField(max_length=45)),
                ('field3', models.CharField(max_length=45)),
                ('field4', models.CharField(max_length=45)),
                ('field5', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker_template',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=45)),
                ('field1', models.CharField(max_length=45)),
                ('field2', models.CharField(max_length=45)),
                ('field3', models.CharField(max_length=45)),
                ('field4', models.CharField(max_length=45)),
                ('field5', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='respond_emergency_call',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AddField(
            model_name='posting',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AddField(
            model_name='note',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AddField(
            model_name='log_tracker',
            name='tracker_id',
            field=models.ForeignKey(to='backend.Tracker'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AddField(
            model_name='disease_hist',
            name='elder_id',
            field=models.ForeignKey(to='backend.Elder'),
        ),
        migrations.AddField(
            model_name='daily_condition',
            name='elder_id',
            field=models.ForeignKey(to='backend.Elder'),
        ),
        migrations.AddField(
            model_name='caregiving',
            name='elder_id',
            field=models.ForeignKey(to='backend.Elder'),
        ),
        migrations.AddField(
            model_name='caregiving',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
        migrations.AddField(
            model_name='admin_invitation',
            name='user_id',
            field=models.ForeignKey(to='backend.User'),
        ),
    ]
