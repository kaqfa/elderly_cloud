from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel, StatusModel

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nama Kategori', max_length=200)
    description = models.TextField('Keterangan', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategori'
        
    def __unicode__(self):
        return self.name

    def __str__(self):  # __unicode__ on Python 2
        return self.__unicode__()

class Article(TimeStampedModel, StatusModel):
    STATUS = (('p','Published'),('a','Archive'))
    
    title = models.CharField('Judul', max_length=200)
    category = models.ManyToManyField(Category, verbose_name="Kategori")
    content = models.TextField('Berita')
    photo = models.ImageField('Foto', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Ditulis Oleh')
    
    class Meta:
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        
    def __unicode__(self):
        return self.title

    def __str__(self):  # __unicode__ on Python 2
        return self.__unicode__()
    
Article._meta.get_field('modified').verbose_name='Waktu'