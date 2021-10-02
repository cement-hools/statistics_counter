from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Event


class EventAddSerializer(ModelSerializer):
    """Сериалайзер добавления события."""

    # date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(ModelSerializer):
    """Сериалайзер добавления события."""

    cpc = serializers.DecimalField(max_digits=19, decimal_places=2)
    cpm = serializers.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        model = Event
        fields = '__all__'
