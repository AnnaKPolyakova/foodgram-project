import json

from django.contrib.flatpages.models import FlatPage
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    help = "load data"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, path, **options):

        with open(path[0]) as file:
            for item in json.load(file):
                FlatPage.objects.get_or_create(
                    id=item["id"],
                    url=item["url"],
                    title=item["title"],
                    content=item["content"],
                )
