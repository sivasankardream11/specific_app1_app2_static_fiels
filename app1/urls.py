from django.urls import path 
from app1.views import *
app_name='prabha1'

urlpatterns=[

    path('specific1/',specific1,name='specific1'),
]