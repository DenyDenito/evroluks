from datetime import datetime
from django.db import models

# Create your models here.

class Promo(models.Model):
    image = models.ImageField(u'Изображение', upload_to='promos/')
    title = models.CharField(u'Наименование', max_length=120)
    description = models.TextField(u'Описание')
    short_description = models.TextField(u'Краткое описание')
    date = models.DateTimeField(u'Дата публикации', default=datetime.now)

    class Meta:
        verbose_name = u'Акция'
        verbose_name_plural = u'Акции'
        ordering = ('-date',)

    def __str__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'promo_detail', (), {"pk": self.pk}
