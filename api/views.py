from decimal import Decimal

from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .filters import CustomFilter, CustomFilter2
from .models import Event2, Event
from .serializers import EventAddSerializer, EventSerializer, Event2Serializer

query = (
    {
        "date": "2021-10-2",
        "views": "10",
        "clicks": "5",
        "cost": "5"
    }
)

@api_view(['GET', 'POST'])
def statistic_clear(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)


class EventListView(ListCreateAPIView):
    queryset = Event.objects.annotate(
        cpc=F('cost') / (F('clicks') * Decimal('1.00')),
        cpm=F('cost') / (F('views') * Decimal('1.00')) * 1000,
    )
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CustomFilter
    filterset_fields = ('date',)
    ordering_fields = '__all__'

    delete_response = {
        'status': status.HTTP_204_NO_CONTENT,
        'data': 'statistic is cleared'
    }

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'PUT',):
            return EventAddSerializer
        return EventSerializer

    def delete(self, request, *args, **kwargs):
        response = self.delete_response
        self.queryset.delete()
        return Response(response, status=status.HTTP_204_NO_CONTENT)


class EventListView2(ListCreateAPIView):
    queryset = Event2.objects.all()
    serializer_class = Event2Serializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = CustomFilter2
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
