RECIPE = "рецепт"
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
