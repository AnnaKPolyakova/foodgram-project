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
    tags = Tag.objects.all()
    if not form.is_valid():
        return render(
            request, 'test3.html', {'form': form, 'tags': tags}
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
        for tag in tags:
            if field == tag.title:
                recipe.tag.add(tag.id)
    recipe.save()
    return redirect('index')


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