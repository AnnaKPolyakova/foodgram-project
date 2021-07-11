from django.contrib.sites.models import Site
from django.core.management import BaseCommand

from config import settings


class Command(BaseCommand):
    help = "load data"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, path, **options):
        site = Site.objects.get(
            id=int(settings.base.SITE_ID),
        )
        site.name = "127.0.0.1:8000"
        site.domain = "127.0.0.1:8000"
        site.save()
