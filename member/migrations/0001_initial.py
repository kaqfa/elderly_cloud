# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminInvitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('status', model_utils.fields.StatusField(default=b'1', max_length=100, verbose_name='status', no_check_for_status=True, choices=[(b'1', b'sent'), (b'2', b'accepted'), (b'3', b'rejected')])),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, verbose_name='status changed', monitor='status')),
                ('email_to_invite', models.CharField(max_length=45)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareGiving',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('address', models.TextField(null=True, blank=True)),
                ('birthday', models.DateField(null=True)),
                ('gender', models.CharField(max_length=1)),
                ('phone', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CareGiver',
            fields=[
                ('member_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='member.Member')),
            ],
            options={
                'abstract': False,
            },
            bases=('member.member',),
        ),
        migrations.CreateModel(
            name='Elder',
            fields=[
                ('member_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='member.Member')),
                ('code', models.CharField(max_length=8)),
                ('cared_by', models.ManyToManyField(to='member.CareGiver', through='member.CareGiving')),
            ],
            options={
                'abstract': False,
            },
            bases=('member.member',),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('member_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='member.Member')),
            ],
            options={
                'abstract': False,
            },
            bases=('member.member',),
        ),
        migrations.AddField(
            model_name='member',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_member.member_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='caregiving',
            name='caregiver',
            field=models.ForeignKey(to='member.CareGiver', null=True),
        ),
        migrations.AddField(
            model_name='caregiving',
            name='elder',
            field=models.ForeignKey(to='member.Elder', null=True),
        ),
    ]
