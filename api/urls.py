from django.urls import path

from api.views import (add_to_favorites, add_to_purchases,
                       delete_from_favorites, delete_from_purchases,
                       getIngredients, profile_follow, profile_unfollow)

urlpatterns = [
    path('ingredients/',
         getIngredients,
         name='api_ingredients'),
    path("subscriptions/",
         profile_follow,
         name="add_favorites"),
    path('subscriptions/<int:author_id>/',
         profile_unfollow,
         name='profile_unfollow'),
    path("purchases/",
         add_to_purchases,
         name="add_to_purchases"),
    path('purchases/<int:recipe_id>/',
         delete_from_purchases,
         name='delete_from_purchases'),
    path("favorites/<int:recipe_id>/",
         delete_from_favorites,
         name="add_favorites"),
    path('favorites/',
         add_to_favorites,
         name='profile_follow'),
]
