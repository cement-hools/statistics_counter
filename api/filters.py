from django_filters import filters
from django_filters.rest_framework import FilterSet

from api.models import Event


class MyFilter(FilterSet):
    """Фильтр для выбора диапазона даты."""
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ('date',)
