from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api),#api bro
    path('live_data.json', views.live_data),#live data bro
    path('chart', views.chart),#chart bro
    ]