from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from recipes.forms import RecipeForm, IngredientsForm
from recipes.models import Recipe, Tag, Ingredient, RecipeIngredientRelation

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
    post_list = Recipe.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, 10)
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
            request, 'test3.html', {'form': form, 'tags_form': Tag.objects.all()}
        )
    form.instance.author = request.user
    recipe = form.save()
    ingredient_order = 0
    for field, value in request.POST.items():
        if field.find(INGREDIENT, 0) != -1:
            field_split = field.split('_')
            RecipeIngredientRelation.objects.create(
                ingredient=get_object_or_404(Ingredient, title=value),
                amount=request.POST[f'{AMOUNT}{field_split[1]}'],
                recipe=recipe,
                ingredient_order=ingredient_order,
            )
            ingredient_order += 1
    return redirect('index')

def get_ingredients(post):
    ingredients = {}
    for key, name in post.items():
        if key.startswith('nameIngredient'):
            num = key.partition('_')[-1]
            ingredients[name] = post[f'valueIngredient_{num}']
    return ingredients


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