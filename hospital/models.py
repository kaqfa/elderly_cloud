from django.db import models
from location_field.models.plain import PlainLocationField

# Create your models here.
class Hospital(models.Model):
    name = models.CharField('Nama', max_length=200)
    address = models.TextField('Alamat', blank=True, null=True)
    phone = models.CharField('Telepon', max_length=20, default="")
    location = PlainLocationField(based_fields=[name],
                                  zoom=7, default='-6.889836,109.674592')
    
    class Meta:
        verbose_name = 'Rumah Sakit'
        verbose_name_plural = 'Rumah Sakit'
        
    def __unicode__(self):
        return self.name

    def __str__(self):  # __unicode__ on Python 2
        return self.__unicode__()