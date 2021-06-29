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
                flatpage = FlatPage.objects.get(
                    id=item["flatpage_id"],
                )
                flatpage.sites.add(settings.base.SITE_ID)
                flatpage.save()
