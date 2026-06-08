from django.urls import path
from .views import time_api

urlpatterns = [
    path('time/', time_api, name='time-api'),
]