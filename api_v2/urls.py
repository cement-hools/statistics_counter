from django.urls import path

from api_v2.views import EventListView

urlpatterns = [
    path('v2/statistic/', EventListView.as_view(), name='statistic_v2'),
]
