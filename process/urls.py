from django.urls import path
from . import views

urlpatterns = [
    path('to_react', views.to_react),#just to test if this function is working
    ]