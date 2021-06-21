from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from api.views import getIngredients, profile_follow, profile_unfollow, \
    delete_from_purchases, add_to_purchases


urlpatterns = [
    # path('', include(router_v1.urls)),
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
    # path("favorites/<int:resipe_id>/",
    #      add_favorites,
    #      name="add_favorites"),
    # path('subscriptions/',
    #      add_favorites,
    #      name='profile_follow'),

]