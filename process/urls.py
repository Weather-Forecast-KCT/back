from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api),#api bro
    path('chart', views.dailychart),#chart bro
    path('live',views.live),#past 1 min data
    path('weather_data',views.weather_data),
    ]