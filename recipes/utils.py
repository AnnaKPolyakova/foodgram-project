from django.shortcuts import get_object_or_404

from recipes.models import (Favorite, Ingredient, Purchase,
                            RecipeIngredientRelation)

RECIPE = "рецепт"
TAG = "tag_"
NUMBER_OR_RECIPES = 3
INGREDIENT = "nameIngredient_"
AMOUNT = "valueIngredient_"


def get_recipes_ending(count):
    if count == 0:
        return None
    elif 0 < count <= NUMBER_OR_RECIPES:
        return "all"
    count = int(str(count)[-1]) - NUMBER_OR_RECIPES
    if count == 1:
        return RECIPE
    elif count in [2, 3, 4]:
        return RECIPE + "a"
    else:
        return RECIPE + "ов"


def get_tag(request):
    tags = []
    for parameter, value in request.GET.items():
        if parameter.find(TAG, 0) != -1:
            tags.append(int(value))
    if len(tags) == 0:
        return None
    return tags


def get_recipe_list(request, values, favorite=False):
    recipe_list = []
    for value in values:
        if favorite is False:
            recipe = value
        else:
            recipe = value.recipe
        recipe_list.append(
            {
                "recipe": recipe,
                "purchase": (
                    request.user.is_authenticated
                    and Purchase.objects.filter(
                        recipe=recipe, user=request.user
                    ).exists()
                ),
                "favorite": (
                    request.user.is_authenticated
                    and Favorite.objects.filter(
                        recipe=recipe, user=request.user
                    ).exists()
                ),
            }
        )
    return recipe_list


def ingredients_check(request):
    count = 0
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            if not Ingredient.objects.filter(title=value).exists():
                return "Можно выбирать только из имеющихся ингредиентов"
            count += 1
            field_split = field.split("_")
            if int(request.POST[f"{AMOUNT}{field_split[1]}"]) <= 0:
                return "Количество ингредиентов не может меньше или равно 0"
    if count == 0:
        return "Обязательное поле."
    return None


def ingredients_get(request):
    ingredients = []
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            field_split = field.split("_")
            if Ingredient.objects.filter(title=value).exists():
                ingredient = Ingredient.objects.filter(title=value)
                amount = request.POST[f"{AMOUNT}{field_split[1]}"]
                ingredients.append({"ingredient": ingredient, "amount": amount})
    return ingredients


def ingredients_save(request, recipe):
    ingredient_order = 0
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            field_split = field.split("_")
            ingredient = get_object_or_404(Ingredient, title=value)
            if not RecipeIngredientRelation.objects.filter(
                ingredient=ingredient, recipe=recipe
            ).exists():
                RecipeIngredientRelation.objects.create(
                    ingredient=ingredient,
                    amount=request.POST[f"{AMOUNT}{field_split[1]}"],
                    recipe=recipe,
                    ingredient_order=ingredient_order,
                )
                ingredient_order += 1
            else:
                recipe_ingredient = get_object_or_404(
                    RecipeIngredientRelation,
                    recipe=recipe,
                    ingredient=ingredient,
                )
                recipe_ingredient.amount = recipe_ingredient.amount + int(
                    request.POST[f"{AMOUNT}{field_split[1]}"]
                )
                recipe_ingredient.save()
