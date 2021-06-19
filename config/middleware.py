from django.shortcuts import get_list_or_404
from django.utils.deprecation import MiddlewareMixin

from recipes.models import Purchase


class CountMiddleware(MiddlewareMixin):

    def process_request(self, request):
        purchase = get_list_or_404(
            Purchase,
            user=request.user,
        )
        request.META['count'] = len(purchase)