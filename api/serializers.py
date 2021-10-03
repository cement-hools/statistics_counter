from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api.models import Event2, Event


class EventAddSerializer(ModelSerializer):
    """Сериалайзер добавления события."""

    # date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Event
        fields = '__all__'


class EventSerializer(ModelSerializer):
    """Сериалайзер списка всех событий."""

    cpc = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)
    cpm = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)

    class Meta:
        model = Event
        fields = '__all__'


class Event2Serializer(ModelSerializer):
    """Сериалайзер списка всех событий."""

    cpc = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)
    cpm = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)

    class Meta:
        model = Event2
        fields = '__all__'
