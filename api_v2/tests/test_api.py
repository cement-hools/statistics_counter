from django.utils.datetime_safe import date
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api_v2.models import Event
from api_v2.serializers import EventSerializer


class EventTestCase(APITestCase):
    def setUp(self):
        event_raw_1 = {
            'date': '2021-10-01',
            'views': 10,
            'clicks': '02',
            'cost': '10.00'
        }
        event_raw_2 = {
            'date': '2021-10-02',
            'views': 21,
            'clicks': 6,
            'cost': '102.01'
        }
        event_raw_3 = {
            'date': '2021-09-30',
            'views': 10,
            'clicks': 10,
            'cost': '5.50'
        }
        event_raw_4 = {
            'date': '2021-09-15',
            'views': '20',
            'clicks': '10',
            'cost': '10.50'
        }

        Event.objects.create(**event_raw_1)
        Event.objects.create(**event_raw_2)
        Event.objects.create(**event_raw_3)
        Event.objects.create(**event_raw_4)

    def test_create_event(self):
        """Создать событие."""
        self.assertEqual(4, Event.objects.all().count(),
                         'Начальное количество событий')
        url = reverse('statistic_v2')
        data = {
            'date': '2020-10-10',
            'views': '20',
            'clicks': '10',
            'cost': '10.50'
        }

        response = self.client.post(url, data=data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code,
                         'Неверный статус ответа')
        self.assertEqual(5, Event.objects.all().count(),
                         'Неверное количество событий после создания')

        new_event = Event.objects.all().last()
        self.assertEqual('2020-10-10', new_event.date.strftime('%Y-%m-%d'),
                         'Неверное значение date у созданного события')
        self.assertEqual(20, new_event.views,
                         'Неверное значение views у созданного события')
        self.assertEqual(10, new_event.clicks,
                         'Неверное значение clicks у созданного события')
        self.assertEqual(10.50, new_event.cost,
                         'Неверное значение cost у созданного события')

    def test_get_list(self):
        """Получаем список всех событий."""
        url = reverse('statistic_v2')
        events = Event.objects.all()

        serializer_data = EventSerializer(events, many=True).data

        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
        self.assertEqual(serializer_data[0].get('cpc'), '17.00')
        self.assertEqual(serializer_data[0].get('cpm'), '4857.62')

    def test_get_ordering_cpm(self):
        """Сортировка по cpm."""
        url = reverse('statistic_v2')
        events = Event.objects.all().order_by('cpm')
        response = self.client.get(url, data={'ordering': 'cpm'})
        serializer_data = EventSerializer(events, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_ordering_cpc(self):
        """Сортировка по cpc."""
        url = reverse('statistic_v2')
        events = Event.objects.all().order_by('cpc')
        response = self.client.get(url, data={'ordering': 'cpc'})
        serializer_data = EventSerializer(events, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter(self):
        """Фильтрация по дате."""
        url = reverse('statistic_v2')
        events = Event.objects.filter(
            date__range=[date(2021, 9, 30), date(2021, 10, 2)]
        )
        response = self.client.get(
            url,
            data={
                'from_date': '2021-09-30',
                'to_date': '2021-10-02',
            }
        )

        serializer_data = EventSerializer(events, many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_filter_sort(self):
        """Фильтрация по дате и сортировка по views."""
        url = reverse('statistic_v2')
        events = Event.objects.filter(
            date__range=[date(2021, 9, 30), date(2021, 10, 2)]
        ).order_by('views')
        response = self.client.get(
            url,
            data={
                'from_date': '2021-09-30',
                'to_date': '2021-10-02',
                'ordering': 'views'
            }
        )
        serializer_data = EventSerializer(events, many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_delete(self):
        self.assertEqual(4, Event.objects.all().count(),
                         'Начальное количество событий')
        url = reverse('statistic_v2')

        response = self.client.delete(url)

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code,
                         'Неверный статус ответа')
        self.assertEqual(0, Event.objects.all().count(),
                         'Неверное количество событий после создания')