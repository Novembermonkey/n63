from django.contrib import admin
from django.urls import path
from app.views import title

urlpatterns = [
    path('title/', title, name='title'),
]