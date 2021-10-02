from decimal import Decimal

from django.db import models
from django.db.models import F, DecimalField, FloatField, Sum
from django.db.models.functions import Cast
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .filters import MyFilter
from .models import Event
from .serializers import EventAddSerializer, EventSerializer

query = (
    {
        "date": "2021-10-2",
        "views": "10",
        "clicks": "5",
        "cost": "5"
    }
)


@api_view(['GET', 'POST'])
def statistic_view(request, *args, **kwargs):
    if request.method == 'GET':
        ordering = request.GET.get('ordering')
        order_by = DEFAUL_ORDERING
        # if ordering:
        #     order_by = ordering

        events = Event.objects.annotate(
            cpc=F('cost') / (F('clicks') * Decimal('1.00')),
            cpm=F('cost') / (F('views') * Decimal('1.00')) * 1000,
        ).order_by(order_by)
        serializer = EventSerializer(instance=events, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = EventAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def statistic_add(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)


@api_view(['GET', 'POST'])
def statistic_clear(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)


class EventListView(generics.ListAPIView):
    queryset = Event.objects.annotate(
            cpc=F('cost') / (F('clicks') * Decimal('1.00')),
            cpm=F('cost') / (F('views') * Decimal('1.00')) * 1000,
        )
    # serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = MyFilter
    filterset_fields = ('date',)
    ordering_fields = '__all__'

    def get_serializer_class(self):
        if self.request.method in ('POST', 'PATCH', 'PUT'):
            return EventAddSerializer
        return EventSerializer
