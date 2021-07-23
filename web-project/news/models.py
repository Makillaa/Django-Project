from django.db import models


class Articles(models.Model):
    title = models.CharField('Article', max_length=50)
    anons = models.CharField('Аnnouncement', max_length=250)
    full_text = models.TextField('Content')
    date = models.DateTimeField('Date of publication')

    def __str__(self):  # возвращаем каждый раз название самого объекта
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
