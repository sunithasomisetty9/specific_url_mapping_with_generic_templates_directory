from django.urls import path
from dc.views import *

app_name='hello'

urlpatterns=[
    path('delhi/',delhi,name='delhi'),
]