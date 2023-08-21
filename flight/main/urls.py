from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
     path('', views.landing, name='landing'),
     path('home', views.home, name='home'),
     path('contact', views.contact, name='contact'),
     path('result', views.result, name='result'),
]