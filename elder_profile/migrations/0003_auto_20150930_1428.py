# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elder_profile', '0002_auto_20150922_1111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diseasehist',
            options={'verbose_name': 'Riwayat Penyakit', 'verbose_name_plural': 'Riwayat Penyakit'},
        ),
        migrations.AlterModelOptions(
            name='medicaltreatmenthist',
            options={'verbose_name': 'Penanganan Kesehatan', 'verbose_name_plural': 'Riwayat Treatment'},
        ),
        migrations.AlterModelOptions(
            name='note',
            options={'verbose_name': 'Catatan', 'verbose_name_plural': 'Data Catatan'},
        ),
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=b'', verbose_name=b'Isi Catatan'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='from_year',
            field=models.IntegerField(default=0, verbose_name=b'Dari Tahun'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='name',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'Nama Penyakit'),
        ),
        migrations.AlterField(
            model_name='diseasehist',
            name='to_year',
            field=models.IntegerField(default=0, verbose_name=b'Hingga Tahun'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='elder',
            field=models.ForeignKey(verbose_name=b'Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='from_year',
            field=models.IntegerField(default=0, verbose_name=b'Dari Tahun'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='to_year',
            field=models.IntegerField(default=0, verbose_name=b'Hingga Tahun'),
        ),
        migrations.AlterField(
            model_name='medicaltreatmenthist',
            name='treatment',
            field=models.TextField(verbose_name=b'Nama Penanganan'),
        ),
        migrations.AlterField(
            model_name='note',
            name='elder',
            field=models.ForeignKey(related_name='for_elder', verbose_name=b'Orang Tua', to='member.Elder'),
        ),
        migrations.AlterField(
            model_name='note',
            name='sharable',
            field=models.CharField(default=b'1', max_length=1, verbose_name=b'Dapat Dibagikan', choices=[(b'1', b'Iya'), (b'0', b'Tidak')]),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=45, verbose_name=b'Judul Catatan'),
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.ForeignKey(related_name='by_user', verbose_name=b'Penulis Catatan', to='member.CareGiver'),
        ),
    ]
