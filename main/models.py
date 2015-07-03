from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(u'Имя', max_length=255)
    phone = models.CharField(u'Телефон', max_length=255)
    message = models.TextField(u'Что нуждается в чистке')
    email = models.EmailField(u'E-mail')
    address = models.CharField(u'Адрес', max_length=255)
    date_execution = models.DateTimeField(u'Удобное время исполнения')
    date = models.DateTimeField(u'Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = u'заявка'
        verbose_name_plural = u'заявки'

    def __str__(self):
        return u'%s' % self.name


class Slide(models.Model):
    image = models.ImageField(upload_to='slides/', name="Image")
    header = models.CharField(u'Заголовок', max_length=120)
    caption = models.CharField(u'Описание', max_length=250, blank=True)

    class Meta:
        verbose_name = u'слайд'
        verbose_name_plural = u'слайды'

    def __str__(self):
        return u'%s' % self.header
