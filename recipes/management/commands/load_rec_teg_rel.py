import json

from django.core.management import BaseCommand

from recipes.models import RecipeTegRelation


class Command(BaseCommand):
    help = 'load data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, path, **options):
        with open(path[0]) as file:
            for item in json.load(file):
                RecipeTegRelation.objects.get_or_create(
                    id=item['id'],
                    recipe_id=item['recipe_id'],
                    teg_id=item['teg_id'],
                )
