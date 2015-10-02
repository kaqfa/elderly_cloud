# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('tracker', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracker',
            options={'verbose_name': 'Penelusuran', 'verbose_name_plural': 'Data Penelusuran'},
        ),
        migrations.AlterField(
            model_name='tracker',
            name='condition',
            field=models.SmallIntegerField(default=3, verbose_name=b'Kondisi',
                                           choices=[(1, b'tidak baik'), (2, b'biasa'), (3, b'baik')]),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Orang Tua', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='photo',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'Gambar'),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='type',
            field=models.CharField(default=b'cd', max_length=2, verbose_name=b'Jenis Penelusuran',
                                   choices=[(b'cd', b'daily condition'), (b'hr', b'heart rate'),
                                            (b'bg', b'blood glucose')]),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='value',
            field=models.SmallIntegerField(default=0, verbose_name=b'Nilai'),
        ),
    ]
