# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160720_1645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='time',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='article.Category', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Judul'),
        ),
    ]
