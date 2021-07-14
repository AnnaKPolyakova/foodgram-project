from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from api.serializers import FavoriteSerializer, FollowSerializer
from recipes.models import Favorite, Follow, Ingredient, Purchase, Recipe
from users.models import User

RESPONSE = JsonResponse({"success": True}, status=status.HTTP_200_OK)
BAD_RESPONSE = JsonResponse(
    {"success": False}, status=status.HTTP_400_BAD_REQUEST
)


@api_view(["GET"])
def get_ingredients(request):
    title = request.GET.get("query", "")
    title = title[:-1]
    ingredient_list = list(
        Ingredient.objects.filter(title__istartswith=title).values(
            "title", "measure"
        )
    )
    return JsonResponse(ingredient_list, safe=False)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def profile_follow(request):
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        author = get_object_or_404(User, id=request.data["id"])
        if author != request.user:
            Follow.objects.get_or_create(
                user=request.user,
                author=get_object_or_404(User, id=request.data["id"]),
            )
            return RESPONSE
    return BAD_RESPONSE


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def profile_unfollow(request, author_id):
    follow = get_object_or_404(Follow, author__id=author_id, user=request.user)
    follow.delete()
    return RESPONSE


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_to_purchases(request):
    serializer = FollowSerializer(data=request.data)
    if serializer.is_valid():
        Purchase.objects.get_or_create(
            user=request.user,
            recipe=get_object_or_404(Recipe, id=request.data["id"]),
        )
        return RESPONSE
    return BAD_RESPONSE


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_from_purchases(request, recipe_id):
    purchase = get_object_or_404(Purchase, recipe=recipe_id, user=request.user)
    purchase.delete()
    return RESPONSE


@api_view(["POST"])
def add_to_favorites(request):
    serializer = FavoriteSerializer(data=request.data)
    if serializer.is_valid():
        Favorite.objects.get_or_create(
            user=request.user,
            recipe=get_object_or_404(Recipe, id=request.data["id"]),
        )
        return RESPONSE
    return BAD_RESPONSE


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_from_favorites(request, recipe_id):
    favorite = get_object_or_404(
        Favorite, recipe__id=recipe_id, user=request.user
    )
    favorite.delete()
    return RESPONSE
