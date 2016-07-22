# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('created', model_utils.fields.AutoCreatedField(verbose_name='created', editable=False, default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(verbose_name='modified', editable=False, default=django.utils.timezone.now)),
                ('status', model_utils.fields.StatusField(choices=[('p', 'Published'), ('a', 'Archive')], verbose_name='status', no_check_for_status=True, default='p', max_length=100)),
                ('status_changed', model_utils.fields.MonitorField(verbose_name='status changed', monitor='status', default=django.utils.timezone.now)),
                ('title', models.CharField(verbose_name='Nama Kegiatan', max_length=200)),
                ('content', models.TextField(blank=True, verbose_name='Berita', null=True)),
                ('photo', models.ImageField(blank=True, verbose_name='Foto', upload_to='', null=True)),
                ('time', models.DateTimeField(blank=True, verbose_name='Tanggal Berita', null=True)),
                ('author', models.OneToOneField(verbose_name='Ditulis Oleh', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Nama Kategori', max_length=200)),
                ('description', models.TextField(blank=True, verbose_name='Keterangan', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='article.Category'),
        ),
    ]
