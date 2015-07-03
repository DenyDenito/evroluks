from datetime import datetime
from django.db import models

# Create your models here.

class BlogEntry(models.Model):
    title = models.CharField(u'Заголовок', max_length=255)
    body = models.TextField(u'Содержание')
    slug = models.SlugField(u'Наименование ссылки', unique=True)
    date = models.DateTimeField(u'Дата публикации', default=datetime.now)
    picture = models.ImageField(u'Изображение', upload_to='blog/')

    class Meta:
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'
        ordering = ('-date',)

    def __str__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return 'blog_detail', (), {'slug': self.slug}
