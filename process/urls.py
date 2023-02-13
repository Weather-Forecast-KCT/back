from django.urls import path
from . import views

urlpatterns = [
    path('to_react', views.to_react),#just to test if this function is working
    path('',views.main),#this is the main body of the backend and this will be used as api
    #the data will only be collected when the api is used somewhere
    ]