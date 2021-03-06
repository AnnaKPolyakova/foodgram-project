import json

from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = "load data"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, path, **options):
        with open(path[0]) as file:
            for item in json.load(file):
                Tag.objects.get_or_create(
                    id=item["id"],
                    title=item["title"],
                    slug=item["slug"],
                    color=item["color"],
                )
