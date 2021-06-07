import json

from django.core.management import BaseCommand

from recipes.models import Ingredient, Measure


class Command(BaseCommand):
    help = 'load data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, path, **options):
        with open(path[0]) as file:
            for item in json.load(file):
                Measure.objects.get_or_create(
                    title=item['dimension'],
                )
        with open(path[0]) as file:
            for item in json.load(file):
                Ingredient.objects.get_or_create(
                    title=item['title'],
                    measure=Measure.objects.get(title=item['dimension']),
                )
