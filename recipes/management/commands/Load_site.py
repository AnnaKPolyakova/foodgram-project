import json

from django.contrib.flatpages.models import FlatPage
from django.contrib.sites.models import Site
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    help = "load data"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, path, **options):
        Site.objects.get_or_create(
            id=int(settings.base.SITE_ID),
            name="127.0.0.1:8000",
            domain="127.0.0.1:8000",
        )
