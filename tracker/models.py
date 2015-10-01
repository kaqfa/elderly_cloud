from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

from member.models import Elder


class Tracker(TimeStampedModel):
    TYPE_CHOICES = (('cd', 'daily condition'), ('hr', 'heart rate'), ('bg', 'blood glucose'))
    CONDITION_CHOICES = ((1, 'tidak baik'), (2, 'biasa'), (3, 'baik'))

    elder = models.ForeignKey(User, verbose_name='Orang Tua')
    condition = models.SmallIntegerField('Kondisi', choices=CONDITION_CHOICES, default=3)
    photo = models.ImageField('Gambar', null=True)
    type = models.CharField('Jenis Penelusuran', max_length=2, choices=TYPE_CHOICES, default='cd')
    value = models.SmallIntegerField('Nilai', default=0)

    class Meta:
        verbose_name = 'Penelusuran'
        verbose_name_plural = 'Data Penelusuran'


    # class LogTracker(models.Model):
    # tracker = models.ForeignKey(Tracker)
    #     value1 = models.IntegerField(default=0)
    #     value2 = models.IntegerField(default=0)
    #     value3 = models.IntegerField(default=0)
    #     value4 = models.IntegerField(default=0)
    #     value5 = models.IntegerField(default=0)