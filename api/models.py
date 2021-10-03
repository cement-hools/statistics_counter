from django.db import models


class Event(models.Model):
    """Событие."""

    date = models.DateField(verbose_name='дата события')
    views = models.PositiveIntegerField(verbose_name='количество показов',
                                        null=True)
    clicks = models.PositiveIntegerField(verbose_name='количество кликов',
                                         null=True)
    cost = models.DecimalField(verbose_name='стоимость кликов',
                               max_digits=19, decimal_places=2, null=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.id} date: {self.date}'


