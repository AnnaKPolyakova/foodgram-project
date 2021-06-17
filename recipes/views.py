from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404
from django.shortcuts import get_object_or_404, redirect, render

from recipes.forms import RecipeForm, IngredientsForm
from recipes.models import Recipe, Tag, Ingredient, RecipeIngredientRelation, Follow
from users.models import User

INGREDIENT = 'nameIngredient_'
AMOUNT = 'valueIngredient_'


def index(request):
    recipe_list = Recipe.objects.all()
    paginator = Paginator(recipe_list, 9)
    page_number = request.GET.get('page')
    tags = Tag.objects.all()
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator, 'tags': tags}
    )


def tag_recipe(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    recipe_list = tag.recipe.all()
    paginator = Paginator(recipe_list, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'tag_recipe.html', {
        'tag': tag,
        'page': page,
        'paginator': paginator,
    })


def follow_index(request):
    follower = request.user.follower.all()
    follower_list = []
    for follow in follower:
        follower_list.append({'author': follow.author,
                              'recipes': follow.author.recipes.all()})
    paginator = Paginator(follower_list, 3)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'myFollow.html', {
        'page': page,
        'paginator': paginator,
    })


def favorite_index(request):
    post_list = Recipe.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'favorite.html', {
        'page': page,
        'paginator': paginator,
    })


def new_recipe(request):
    form = RecipeForm(request.POST or None, files=request.FILES or None)
    if not form.is_valid():
        return render(
            request, 'new_recipe.html', {'form': form}
        )
    form.instance.author = request.user
    recipe = form.save()
    ingredient_order = 0
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            field_split = field.split('_')
            ingredient = get_object_or_404(Ingredient, title=value)
            if not RecipeIngredientRelation.objects.filter(
                    ingredient=ingredient, recipe=recipe).exists():
                RecipeIngredientRelation.objects.create(
                    ingredient=ingredient,
                    amount=request.POST[f'{AMOUNT}{field_split[1]}'],
                    recipe=recipe,
                    ingredient_order=ingredient_order,
                )
                ingredient_order += 1
            else:
                recipe_ingredient = get_object_or_404(
                    RecipeIngredientRelation, recipe=recipe,
                                               ingredient=ingredient)
                recipe_ingredient.amount = recipe_ingredient.amount + int(
                    request.POST[f'{AMOUNT}{field_split[1]}'])
                recipe_ingredient.save()
    recipe.save()
    return redirect('index')


def recipe_edit(request, username, recipe_id):
    if request.user.username != username:
        return redirect('recipe', username, recipe_id)
    recipe_old = get_object_or_404(Recipe, author__username=username,
                                 id=recipe_id)

    form = RecipeForm(data=request.POST or None,
                      files=request.FILES or None,
                      instance=recipe_old)
    ingredients = RecipeIngredientRelation.objects.filter(recipe=recipe_old)
    if not form.is_valid():
        return render(
            request, 'new_recipe.html', {'form': form,
                                         'recipe': recipe_old,
                                         'ingredients': ingredients}
        )
    ingredients_old = get_list_or_404(RecipeIngredientRelation,
                                      recipe=recipe_old)
    for ingredient in ingredients_old:
        ingredient.delete()
    form.instance.author = request.user
    recipe = form.save()
    ingredient_order = 0
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            field_split = field.split('_')
            ingredient = get_object_or_404(Ingredient, title=value)
            if not RecipeIngredientRelation.objects.filter(
                    ingredient=ingredient, recipe=recipe_old).exists():
                RecipeIngredientRelation.objects.create(
                    ingredient=ingredient,
                    amount=request.POST[f'{AMOUNT}{field_split[1]}'],
                    recipe=recipe,
                    ingredient_order=ingredient_order,
                )
                ingredient_order += 1
            else:
                recipe_ingredient = get_object_or_404(
                    RecipeIngredientRelation, recipe=recipe_old,
                                               ingredient=ingredient)
                recipe_ingredient.amount = recipe_ingredient.amount + int(
                    request.POST[f'{AMOUNT}{field_split[1]}'])
                recipe_ingredient.save()
    recipe.save()
    return redirect('recipe',username=username,recipe_id=recipe_id)


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    ingredients = RecipeIngredientRelation.objects.filter(recipe=recipe)
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'author': recipe.author,
        'ingredients': ingredients,
    })


def recipe_delete(request, username, recipe_id):
    recipe = get_object_or_404(
        Recipe,
        author=request.user,
        id=recipe_id
    )
    if recipe.author == request.user:
        recipe.delete()
        return redirect('index')


def author_page(request, username):
    author = get_object_or_404(User, username=username)
    recipe_list = author.recipes.all()
    tags = Tag.objects.all()
    paginator = Paginator(recipe_list, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    following = (request.user.is_authenticated and
                 author != request.user and
                 Follow.objects.filter(author=author,
                                       user=request.user).exists())
    return render(request, 'author_page.html', {
        'author': author,
        'page': page,
        'tags': tags,
        'paginator': paginator,
        'following': following,
    })


def shop_list(request):
    post_list = Recipe.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'shopList.html',
        {'page': page, 'paginator': paginator}
    )