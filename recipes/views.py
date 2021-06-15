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
            request, 'new_recipe.html', {'form': form}
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
    recipe.save()
    return redirect('index')

#
# def post_edit(request, username, post_id):
#     if request.user.username != username:
#         return redirect('post', username, post_id)
#     post = get_object_or_404(Post,
#                              id=post_id,
#                              author__username=username)
#     form = PostForm(request.POST or None,
#                     files=request.FILES or None,
#                     instance=post)
#     if not form.is_valid():
#         return render(request, "new_post.html", {'form': form, 'post': post})
#     form.instance.author = request.user
#     form.save()
#     return redirect('post', username, post_id)


def recipe_edit(request, username, recipe_id):
    if request.user.username != username:
        return redirect('recipe', username, recipe_id)
    recipe = get_object_or_404(
        Recipe,
        id=recipe_id,
    )
    form = RecipeForm(data=request.GET or None,
                      files=request.FILES or None,
                      instance=recipe)
    ingredients = RecipeIngredientRelation.objects.filter(recipe=recipe)
    if not form.is_valid():
        return render(
            request, 'new_recipe.html', {'form': form,
                                         'recipe': recipe,
                                         'ingredients': ingredients}
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
    recipe.save()
    return redirect('index')


def recipe_view(request, username, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author__username=username)
    return render(request, 'recipe.html', {
        'recipe': recipe,
        'author': recipe.author,
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