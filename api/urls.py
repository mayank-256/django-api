from django.urls import path
from .views import time_api
from .views import hello_api

urlpatterns = [
    path('hello/', hello_api, name='hello-api'),
    path('time/', time_api, name='time-api'),

]