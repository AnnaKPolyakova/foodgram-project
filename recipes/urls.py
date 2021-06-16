from django.contrib import admin
from django.urls import path
from .api import profile_follow, profile_unfollow

from . import views
from .api import getIngredients

urlpatterns = [
    path('',
         views.index,
         name='index'
         ),
    path('subscriptions/',
         profile_follow,
         name='profile_follow'),
    path('subscriptions/<int:follow_id>/',
         profile_unfollow,
         name='profile_unfollow'),
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
    path('ingredients/',
         getIngredients,
         name='api_ingredients'),
    path('<str:username>/<int:recipe_id>/edit/',
         views.recipe_edit,
         name='recipe_edit'),
    path('<str:username>/<int:recipe_id>/',
         views.recipe_view,
         name='recipe'),
    path('<str:username>/<int:recipe_id>/delete/',
         views.recipe_delete,
         name='recipe_delete'),
    path('<str:username>/',
         views.author_page,
         name='author_page'),
]

