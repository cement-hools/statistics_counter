from rest_framework import mixins, status
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class CustomViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    GenericAPIView):
    """Кастомный ViewSet."""

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


