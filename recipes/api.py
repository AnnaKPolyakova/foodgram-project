from rest_framework.decorators import api_view
from django.http import JsonResponse


from recipes.models import Ingredient


@api_view(['GET'])
def getIngredients(request):
    title = request.GET.get('query', '')
    title = title[:-1]
    ingredient_list = list(
        Ingredient.objects.filter(title__istartswith=title)
        .values('title', 'measure')
    )
    return JsonResponse(ingredient_list, safe=False)
