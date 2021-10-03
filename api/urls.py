from django.urls import path

from api.views import EventListView

urlpatterns = [
    path('v1/statistic/', EventListView.as_view(), name='statistic'),
]
