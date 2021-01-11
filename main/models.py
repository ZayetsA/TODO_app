from django.db import models


class Task(models.Model):
    objects = None
    title = models.CharField('Name', max_length=30)
    task = models.TextField('Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
