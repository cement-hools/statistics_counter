from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from api_v2.models import Event


class EventSerializer(ModelSerializer):
    """Сериалайзер событий."""

    cpc = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)
    cpm = serializers.DecimalField(max_digits=19, decimal_places=2,
                                   read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
