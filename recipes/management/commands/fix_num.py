from django.core.management.color import no_style
from django.db import connection

from recipes.models import (
    Recipe,
    Tag,
    Ingredient,
    RecipeIngredientRelation,
    Follow,
    Favorite,
    Purchase
)
from users.models import User

sequence_sql = connection.ops.sequence_reset_sql(
    no_style(), [
        Recipe,
        User,
        Tag,
        Ingredient,
        RecipeIngredientRelation,
        Follow,
        Favorite,
        Purchase
    ]
)
with connection.cursor() as cursor:
    for sql in sequence_sql:
        cursor.execute(sql)