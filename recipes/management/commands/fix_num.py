from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection

from recipes.models import (Favorite, Follow, Ingredient, Purchase, Recipe,
                            RecipeIngredientRelation, Tag)
from users.models import User

sequence_sql = connection.ops.sequence_reset_sql(
    no_style(),
    [
        Recipe,
        User,
        Tag,
        Ingredient,
        RecipeIngredientRelation,
        Follow,
        Favorite,
        Purchase,
    ],
)


class Command(BaseCommand):
    help = "load data"

    def add_arguments(self, parser):
        parser.add_argument("path", nargs="+", type=str)

    def handle(self, path, **options):
        with connection.cursor() as cursor:
            for sql in sequence_sql:
                cursor.execute(sql)
