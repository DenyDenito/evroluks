from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(u'Наименование', max_length=255)
    caption = models.CharField(u'Описание', max_length=1000, blank=True)

    class Meta:
        verbose_name = u'Альбом'
        verbose_name_plural = u'Альбомы'

    def __str__(self):
        return u'%s' % self.title


class Image(models.Model):
    picture = models.ImageField(u'Изображение', upload_to='gallery/')
    title = models.CharField(u'Наименование', max_length=255, blank=True)
    description = models.CharField(u'Описание', max_length=1000, blank=True)
    album = models.ForeignKey(Album, verbose_name=u'Альбом')

    class Meta:
        verbose_name = u'Фотография'
        verbose_name_plural = u'Фотографии'

    def __str__(self):
        return u'%s' % self.title
