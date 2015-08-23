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
            name='DailyCondition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.CharField(max_length=1)),
                ('time_record', models.DateTimeField()),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseHist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disease', models.CharField(max_length=45)),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalTreatmentHist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('treatment', models.TextField()),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=45)),
                ('dosage', models.CharField(max_length=45)),
                ('elder', models.ForeignKey(to='member.Elder')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('elder', models.ForeignKey(to='member.Elder')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
