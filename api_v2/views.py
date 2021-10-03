from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from api_v2.filters import CustomFilter
from api_v2.models import Event
from api_v2.serializers import EventSerializer


class EventListView(ListCreateAPIView):
    """
    Версия 2
    Показать все записи статистики событий.
    Поля:
        date - дата события (обязательное поле)
        views - количество показов (опционально)
        clicks - количество кликов (опционально)
        cost - стоимость кликов (опционально, в рублях с точностью до копеек)
        cpc - cost/clicks (средняя стоимость клика)
        cpm - cost/views * 1000 (средняя стоимость 1000 показов)
    Параметры запроса:
        Формат даты: YYYY-MM-DD
        - date: string - вывести статистику по событию за указанную дату
        - from_date: string - вывести статистику по событиям начиная с указанной даты
        - to_date: string - вывести статистику по событиям по указанную дату
        - date_range: string - статистика за период.
        - ordering: string - отсортировать события по выбранному полю (доступны все поля)
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CustomFilter
    filterset_fields = ('date',)
    ordering_fields = '__all__'

    delete_response = {
        'status': status.HTTP_204_NO_CONTENT,
        'data': 'statistic is cleared'
    }

    def delete(self, request, *args, **kwargs):
        response = self.delete_response
        self.queryset.delete()
        return Response(response, status=status.HTTP_204_NO_CONTENT)
