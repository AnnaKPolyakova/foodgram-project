from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect, render

from recipes.forms import RecipeForm
from recipes.models import Recipe


def index(request):
    post_list = Recipe.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'index.html',
        {'page': page, 'paginator': paginator}
    )


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
        return render(request, 'new_recipe.html', {'form': form})
    form.instance.author = request.user
    form.save()
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