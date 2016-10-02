from django.db import models
from django.db.models import Q
from model_utils.models import TimeStampedModel
from location_field.models.plain import PlainLocationField
from datetime import datetime, date, time
from datetime import timedelta

from member.models import Elder


class TrackerManager(models.Manager):
    def get_queryset(self):
        return super(TrackerManager, self).get_queryset().order_by('-created')


class Tracker(TimeStampedModel):
    TYPE_CHOICES = (('dc', 'daily condition'),
                    ('hr', 'heart rate'),
                    ('bg', 'blood glucose'))
    CONDITION_CHOICES = (('ba', 'baik'), ('bi', 'kangen'), ('tb', 'panik'),
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
                         ('str', 'sakit telapak kaki kanan'),
                         ('ltl', 'sakit lutut kiri'),
                         ('ltr', 'sakit lutut kanan'))

    elder = models.ForeignKey(Elder, verbose_name='Orang Tua')
    type = models.CharField('Jenis Penelusuran', max_length=2,
                            choices=TYPE_CHOICES, default='dc')
    condition = models.CharField('Kondisi', max_length=3,
                                 choices=CONDITION_CHOICES, default='ba')
    value = models.SmallIntegerField('Nilai', default=0)
    photo = models.ImageField('Gambar', null=True, blank=True)
    location = PlainLocationField(based_fields=[elder],
                                  zoom=7, default='-6.889836,109.674592')

    objects = TrackerManager()

    class Meta:
        verbose_name = 'Penelusuran'
        verbose_name_plural = 'Data Penelusuran'

    @staticmethod
    def today_tracking():
        today = datetime.now().date()
        today_start = datetime.combine(today, time())
        return Tracker.objects.filter(created__gte = today_start)

    @staticmethod
    def today_member_not_tracking():
        today_tracking = Tracker.today_tracking().values_list('elder_id', flat = True)
        return Elder.objects.exclude(id__in = today_tracking)

    def __unicode__(self):
        return str(self.elder)+'-'+self.get_condition_display()

    def __str__(self):
        return self.__unicode__()



class ConditionManager(models.Manager):
    def get_queryset(self):
        return super(ConditionManager, self).get_queryset().filter(~Q(condition='tb'))


class PanicManager(models.Manager):
    def get_queryset(self):
        return super(PanicManager, self).get_queryset().filter(condition='tb')


class TrackCondition(Tracker):
    objects = ConditionManager()

    class Meta:
        proxy = True


class TrackPanic(Tracker):
    objects = PanicManager()

    class Meta:
        proxy = True