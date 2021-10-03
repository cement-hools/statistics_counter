from django.db import models


class Event(models.Model):
    """Событие."""

    date = models.DateField(verbose_name='дата события')
    views = models.PositiveIntegerField(verbose_name='количество показов',
                                        null=True, blank=True)
    clicks = models.PositiveIntegerField(verbose_name='количество кликов',
                                         null=True, blank=True)
    cost = models.DecimalField(verbose_name='стоимость кликов',
                               max_digits=19, decimal_places=2, null=True,
                               blank=True)
    cpc = models.DecimalField(verbose_name='средняя стоимость клика',
                              max_digits=19, decimal_places=2, null=True,
                              blank=True)
    cpm = models.DecimalField(verbose_name='средняя стоимость 1000 показов',
                              max_digits=19, decimal_places=2, null=True,
                              blank=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'
        ordering = ('-date',)

    def __str__(self):
        return f'{self.id} date: {self.date}, cpc {self.cpc}'

    def save(self, *args, **kwargs):
        cpc = cpm = None
        if self.cost and self.clicks:
            cpc = float(self.cost) / float(self.clicks)
        if self.cost and self.views:
            cpm = float(self.cost) / float(self.views) * 1000

        self.cpc = cpc
        self.cpm = cpm
        super().save(*args, **kwargs)
