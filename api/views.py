from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def statistic_view(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)


@api_view(['GET', 'POST'])
def statistic_add(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)


@api_view(['GET', 'POST'])
def statistic_clear(request, *args, **kwargs):
    response = {'status': 'fail'}
    return Response(response, 400)
