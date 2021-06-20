import json

from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from users.models import User


from recipes.models import Ingredient, Follow, Favorite, Recipe


@api_view(['GET'])
def getIngredients(request):
    title = request.GET.get('query', '')
    title = title[:-1]
    ingredient_list = list(
        Ingredient.objects.filter(title__istartswith=title)
        .values('title', 'measure')
    )
    return JsonResponse(ingredient_list, safe=False)


@api_view(['POST'])
def profile_follow(request):
    author_id = json.loads(request.body)['id']
    author = get_object_or_404(User, id=author_id)
    if author != request.user and not Follow.objects.filter(
            author=author,
            user=request.user).exists():
        follow = Follow.objects.create(
            user=request.user,
            author=author,
        )
        return {'id': str(follow.id)}


@api_view(['DELETE'])
def profile_unfollow(request, id):
    follow = get_object_or_404(Follow,
                               author__id=id,
                               user=request.user)
    follow.delete()
    return {}


@api_view(['POST'])
def add_favorites(request):
    recipe_id = json.loads(request.body)['id']
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe.user != request.user and not Favorite.objects.filter(
            recipe=recipe,
            user=request.user).exists():
        follow = Favorite.objects.create(
            user=request.user,
            recipe=recipe_id,
        )
        return {'id': str(follow.id)}
