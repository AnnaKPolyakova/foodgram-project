from django.core.paginator import Paginator
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import (get_list_or_404, get_object_or_404, redirect,
                              render)

from recipes.forms import RecipeForm
from recipes.models import (Favorite, Follow, Ingredient, Purchase, Recipe,
                            RecipeIngredientRelation, Tag)
from recipes.utils import (NUMBER_OR_RECIPES, get_recipe_list,
                           get_recipes_ending, get_tag)
from users.models import User

INGREDIENT = "nameIngredient_"
AMOUNT = "valueIngredient_"


def index(request):
    request_tag = get_tag(request)
    tags = Tag.objects.all()
    if request_tag is None:
        recipes = Recipe.objects.all()
    else:
        recipes = Recipe.objects.filter(tags__in=request_tag).distinct()
    recipe_list = get_recipe_list(request, recipes)
    paginator = Paginator(recipe_list, 9)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "index.html",
        {
            "page": page,
            "paginator": paginator,
            "tags": tags,
            "request_tag": request_tag,
        },
    )


def tag_recipe(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    recipe_list = tag.recipe.all()
    paginator = Paginator(recipe_list, 5)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "tag_recipe.html",
        {
            "tag": tag,
            "page": page,
            "paginator": paginator,
        },
    )


def follow_index(request):
    follower = request.user.follower.all()
    follower_list = []
    for follow in follower:
        follower_list.append(
            {
                "author": follow.author,
                "recipes": follow.author.recipes.all()[:NUMBER_OR_RECIPES],
                "count": follow.author.recipes.count() - NUMBER_OR_RECIPES,
                "recipes_info": get_recipes_ending(
                    follow.author.recipes.count()
                ),
            }
        )
    paginator = Paginator(follower_list, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "myFollow.html",
        {
            "page": page,
            "paginator": paginator,
        },
    )


def favorite_index(request):
    tags = Tag.objects.all()
    request_tag = get_tag(request)
    if request_tag is not None:
        favorites = Favorite.objects.filter(
            recipe__tags__in=request_tag, user=request.user
        ).distinct()
    else:
        favorites = get_list_or_404(Favorite, user=request.user)
    recipes = get_recipe_list(request, favorites, favorite=True)
    paginator = Paginator(recipes, 3)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request,
        "favorite.html",
        {
            "page": page,
            "paginator": paginator,
            "tags": tags,
            "request_tag": request_tag,
        },
    )


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


def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(request, "recipe_add_edit.html", {"form": form})
    form.instance.author = request.user
    recipe = form.save()
    ingredients_save(request, recipe)
    recipe.save()
    return redirect("index")


def recipe_edit(request, username, recipe_id):
    if request.user.username != username:
        return redirect("recipe", username, recipe_id)
    recipe_old = get_object_or_404(
        Recipe, author__username=username, id=recipe_id
    )

    form = RecipeForm(
        data=request.POST or None,
        files=request.FILES or None,
        instance=recipe_old,
    )
    ingredients = RecipeIngredientRelation.objects.filter(recipe=recipe_old)
    if not form.is_valid():
        return render(
            request,
            "recipe_add_edit.html",
            {"form": form, "recipe": recipe_old, "ingredients": ingredients},
        )
    RecipeIngredientRelation.objects.filter(recipe=recipe_old).delete()
    form.instance.author = request.user
    recipe = form.save()
    ingredients_save(request, recipe_old)
    recipe.save()
    return redirect("recipe", username=username, recipe_id=recipe_id)


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    ingredients = RecipeIngredientRelation.objects.filter(recipe=recipe)
    return render(
        request,
        "recipe.html",
        {
            "recipe": recipe,
            "author": recipe.author,
            "ingredients": ingredients,
            "purchase": request.user.is_authenticated
            and Purchase.objects.filter(
                recipe=recipe, user=request.user
            ).exists(),
            "following": request.user.is_authenticated
            and Follow.objects.filter(
                author=recipe.author, user=request.user
            ).exists(),
            "favorite": request.user.is_authenticated
            and Favorite.objects.filter(
                recipe=recipe, user=request.user
            ).exists(),
        },
    )


def recipe_delete(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, author=request.user, id=recipe_id)
    if recipe.author == request.user:
        recipe.delete()
    return redirect("index")


def author_page(request, username):
    request_tag = get_tag(request)
    author = get_object_or_404(User, username=username)
    if request_tag is None:
        recipes = author.recipes.all()
    else:
        recipes = Recipe.objects.filter(
            tag__in=request_tag,
            author=author
        ).distinct()
    tags = Tag.objects.all()
    recipe_list = get_recipe_list(request, recipes)
    paginator = Paginator(recipe_list, 9)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    following = (
        request.user.is_authenticated
        and author != request.user
        and Follow.objects.filter(author=author, user=request.user).exists()
    )
    return render(
        request,
        "author_page.html",
        {
            "author": author,
            "page": page,
            "tags": tags,
            "paginator": paginator,
            "following": following,
            "request_tag": request_tag,
        },
    )


def shop_list(request):
    purchase_list = request.user.purchase.all()
    paginator = Paginator(purchase_list, 10)
    page_number = request.GET.get("page")
    page = paginator.get_page(page_number)
    return render(
        request, "shopList.html", {"page": page, "paginator": paginator}
    )


def shop_list_delete(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    purchase = get_object_or_404(
        Purchase,
        recipe=recipe,
    )
    purchase.delete()
    return redirect("shop_list")


def shop_list_download(request):
    filename = "purchase.txt"
    recipes = Recipe.objects.filter(purchase__user=request.user)
    ingredients = (
        RecipeIngredientRelation.objects.filter(recipe__in=recipes)
        .values("ingredient__title", "ingredient__measure")
        .annotate(amount=Sum("amount"))
    )
    content = [
        f'{ingredient["ingredient__title"]} {ingredient["amount"]} '
        f'{ingredient["ingredient__measure"]} \n'
        for ingredient in ingredients
    ]
    response = HttpResponse(content, content_type="text/plain")
    response["Content-Disposition"] = "attachment; filename={0}".format(
        filename
    )
    return response
