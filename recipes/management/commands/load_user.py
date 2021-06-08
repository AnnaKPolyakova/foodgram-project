import json

from django.core.management import BaseCommand

from recipes.models import User


class Command(BaseCommand):
    help = 'load data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, path, **options):
        with open(path[0]) as file:
            for item in json.load(file):
                User.objects.get_or_create(
                    id=item['id'],
                    username=item['username'],
                    password=item['password'],
                    is_superuser=True,
                    is_staff=True,
                    is_active=True,
                )
