from django.urls import path


from api.views import getIngredients, add_favorites
from api.views import profile_follow, profile_unfollow


urlpatterns = [
    path('ingredients/',
         getIngredients,
         name='api_ingredients'),
    path("favorites/",
         add_favorites,
         name="add_favorites"),
    path("favorites/<int:resipe_id>/",
         add_favorites,
         name="add_favorites"),
    path('subscriptions/',
         profile_follow,
         name='profile_follow'),
    path('subscriptions/<int:author_id>/',
         profile_unfollow,
         name='profile_unfollow'),
]