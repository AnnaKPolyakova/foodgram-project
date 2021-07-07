from recipes.models import Purchase, Favorite

RECIPE = "рецепт"
TAG = "tag_"
NUMBER_OR_RECIPES = 3


def get_recipes_ending(count):
    if count == 0:
        return None
    elif 0 < count <= NUMBER_OR_RECIPES:
        return "all"
    count = str(count)[-1]
    if count == "1":
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
