from django.urls import path
from . import views

urlpatterns = [
    path('api', views.api),#just to test if this function is working
    ]