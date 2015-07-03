from django.db import models

# Create your models here.

class Service(models.Model):
    image = models.ImageField(u'Изображение', upload_to='services/')
    title = models.CharField(u'Наименование', max_length=120)
    description = models.TextField(u'Описание')
    short_description = models.TextField(u'Краткое описание')

    class Meta:
        verbose_name = u'Услуга'
        verbose_name_plural = u'Услуги'

    def __str__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'service_detail', (), {"pk": self.pk}