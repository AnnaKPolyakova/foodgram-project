from django.core.paginator import Paginator
from django.shortcuts import render

from recipes.models import Recipe


def index(request):
    post_list = Recipe.objects.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(
        request,
        'indexAuth.html',
        {'page': page, 'paginator': paginator}
    )