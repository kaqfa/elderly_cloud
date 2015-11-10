# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0004_auto_20151001_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasehist',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='from_year',
            field=models.IntegerField(verbose_name='Dari Tahun', default=2015),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='name',
            field=models.CharField(verbose_name='Nama Penyakit', max_length=200, default=''),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='to_year',
            field=models.IntegerField(verbose_name='Hingga Tahun', default=2015),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='from_year',
            field=models.IntegerField(verbose_name='Dari Tahun', default=0),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='to_year',
            field=models.IntegerField(verbose_name='Hingga Tahun', default=0),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='treatment',
            field=models.TextField(verbose_name='Nama Penanganan'),
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(verbose_name='Isi Catatan', default=''),
        ),
        migrations.AlterField(
            model_name='note',
            name='elder',
            field=models.ForeignKey(verbose_name='Orang Tua', related_name='for_elder', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='note',
            name='sharable',
            field=models.CharField(verbose_name='Dapat Dibagikan', choices=[('1', 'Iya'), ('0', 'Tidak')], max_length=1, default='1'),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(verbose_name='Judul Catatan', max_length=45),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(verbose_name='Penulis Catatan', related_name='by_user', to='member.CareGiver'),
        ),
    ]
