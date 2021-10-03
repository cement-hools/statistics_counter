from django.urls import path

from api.views import statistic_view, EventListView

urlpatterns = [
    path('v1/', statistic_view, name='statistic_view'),
    path('v2/', EventListView.as_view(), name='event'),
    ]
