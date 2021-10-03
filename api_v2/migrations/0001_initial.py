# Generated by Django 3.2.7 on 2021-10-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='дата события')),
                ('views', models.PositiveIntegerField(blank=True, null=True, verbose_name='количество показов')),
                ('clicks', models.PositiveIntegerField(blank=True, null=True, verbose_name='количество кликов')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='стоимость кликов')),
                ('cpc', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='средняя стоимость клика')),
                ('cpm', models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True, verbose_name='средняя стоимость 1000 показов')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистика',
                'ordering': ('-date',),
            },
        ),
    ]
