from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse

from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated

from users.models import User

from recipes.models import Ingredient, Follow, Favorite, Recipe, Purchase

RESPONSE = JsonResponse({'success': True}, status=status.HTTP_200_OK)
BAD_RESPONSE = JsonResponse(
    {'success': False},
    status=status.HTTP_400_BAD_REQUEST
)


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
@permission_classes([IsAuthenticated])
def profile_follow(request):
    author_id = request.data['id']
    author = get_object_or_404(User, id=author_id)
    if author != request.user and not Follow.objects.filter(
            author=author,
            user=request.user).exists():
        follow = Follow.objects.create(
            user=request.user,
            author=author,
        )
        return RESPONSE
    return BAD_RESPONSE


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def profile_unfollow(request, author_id):
    follow = get_object_or_404(Follow,
                               author__id=author_id,
                               user=request.user)
    follow.delete()
    return RESPONSE


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_purchases(request):
    recipe_id = request.data['id']
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if not Purchase.objects.filter(
            recipe=recipe.id,
            user=request.user.id).exists():
        purchase = Purchase.objects.create(
            user=request.user,
            recipe=recipe,
        )
        return RESPONSE
    return BAD_RESPONSE


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_from_purchases(request, recipe_id):
    purchase = get_object_or_404(Purchase,
                               recipe=recipe_id,
                               user=request.user)
    purchase.delete()
    return RESPONSE


# @api_view(['POST'])
# def add_favorites(request):
#     recipe_id = json.loads(request.body)['id']
#     recipe = get_object_or_404(Recipe, id=recipe_id)
#     if recipe.user != request.user and not Favorite.objects.filter(
#             recipe=recipe,
#             user=request.user).exists():
#         follow = Favorite.objects.create(
#             user=request.user,
#             recipe=recipe_id,
#         )
#         return {'id': str(follow.id)}
