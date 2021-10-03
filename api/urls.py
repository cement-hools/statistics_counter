from django.urls import path

from api.views import EventListView, EventListView2

urlpatterns = [
    path('v1/statistic/', EventListView.as_view(), name='event'),
    path('v2/statistic/', EventListView2.as_view(), name='event_v2'),
    ]
