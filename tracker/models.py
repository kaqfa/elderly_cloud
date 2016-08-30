from django.db import models
from model_utils.models import TimeStampedModel
from location_field.models.plain import PlainLocationField

from member.models import Elder


class Tracker(TimeStampedModel):
    TYPE_CHOICES = (('dc', 'daily condition'),
                    ('hr', 'heart rate'),
                    ('bg', 'blood glucose'))
    CONDITION_CHOICES = (('ba', 'baik'), ('bi', 'kangen'), ('tb', 'tidak baik'),
                         ('sk', 'sakit kepala'),
                         ('sl', 'sakit leher'),
                         ('sdl', 'sakit dada kiri'),
                         ('sdr', 'sakit dada kanan'),
                         ('sal', 'sakit lengan atas kiri'),
                         ('sar', 'sakit lengan atas kanan'),
                         ('sll', 'sakit lengan kiri'),
                         ('slr', 'sakit lengan kanan'),
                         ('sp', 'sakit perut'),
                         ('spl', 'sakit paha kiri'),
                         ('spr', 'sakit paha kanan'),
                         ('sbl', 'sakit betis kiri'),
                         ('sbr', 'sakit betis kanan'),
                         ('stl', 'sakit telapak kaki kiri'),
                         ('str', 'sakit telapak kaki kanan'))

    elder = models.ForeignKey(Elder, verbose_name='Orang Tua')
    type = models.CharField('Jenis Penelusuran', max_length=2,
                            choices=TYPE_CHOICES, default='dc')
    condition = models.CharField('Kondisi', max_length=3,
                                 choices=CONDITION_CHOICES, default='ba')
    value = models.SmallIntegerField('Nilai', default=0)
    photo = models.ImageField('Gambar', null=True, blank=True)
    location = PlainLocationField(based_fields=[elder],
                                  zoom=7, default='-6.889836,109.674592')

    class Meta:
        verbose_name = 'Penelusuran'
        verbose_name_plural = 'Data Penelusuran'

    def __unicode__(self):
        return str(self.elder)+'-'+self.get_condition_display()

    def __str__(self):
        return self.__unicode__()
