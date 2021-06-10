from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',
         views.index,
         name='index'),
    path("follow/",
         views.follow_index,
         name="follow_index"),
    path("favorite/",
         views.favorite_index,
         name="favorite_index"),
    path('new_recipe/',
         views.new_recipe,
         name='new_recipe'),
    path('shop_list/',
         views.shop_list,
         name='shop_list'),
    path('tag/<slug:slug>/',
         views.tag_recipe,
         name='tag_recipe'),
]