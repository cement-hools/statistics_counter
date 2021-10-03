from django_filters import filters
from django_filters.rest_framework import FilterSet

from api.models import Event


class CustomFilter(FilterSet):
    """Фильтр для выбора диапазона даты."""
    from_date = filters.DateFilter(field_name='date', lookup_expr='gte',
                                   label='From')
    to_date = filters.DateFilter(field_name='date', lookup_expr='lte',
                                 label='To')
    date_range = filters.DateRangeFilter(field_name='date', label='Range')

    class Meta:
        model = Event
        fields = ('date',)
