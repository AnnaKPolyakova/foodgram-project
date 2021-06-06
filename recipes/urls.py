from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("follow/",
         views.follow_index,
         name="follow_index"),
]