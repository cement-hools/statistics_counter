from django.urls import path

from api.views import statistic_view

urlpatterns = [
    path('v1/', statistic_view, name='statistic_view'),
]
