from django.urls import path
from rcb.views import *

app_name='hi'

urlpatterns=[
    path('banglore/',banglore,name='banglore'),
]