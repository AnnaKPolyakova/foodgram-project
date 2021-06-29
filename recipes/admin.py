from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from recipes.models import (
    Favorite,
    Follow,
    Ingredient,
    Purchase,
    Recipe,
    RecipeIngredientRelation,
    Tag,
)
from users.models import User


class PurchaseInline(admin.TabularInline):
    model = Purchase


class FollowInline(admin.TabularInline):
    model = Follow
    fk_name = "user"


class FavoriteInline(admin.TabularInline):
    model = Favorite


class CustomUserAdmin(UserAdmin):
    inlines = [
        FavoriteInline,
        FollowInline,
        PurchaseInline,
    ]

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_superuser", "is_staff"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


class RecipeIngredientLine(SortableInlineAdminMixin, admin.TabularInline):
    model = RecipeIngredientRelation
    verbose_name_plural = "Доп. информация"


class TagAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
    )
    search_fields = (
        "title",
        "slug",
    )
    empty_value_display = "-пусто-"


class MeasureAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    empty_value_display = "-пусто-"


class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "measure",
    )
    search_fields = (
        "title",
        "measure",
    )
    empty_value_display = "-пусто-"


class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ("tags",)
    inlines = (RecipeIngredientLine,)
    list_display = (
        "title",
        "author",
        "time",
        "pub_date",
    )
    search_fields = (
        "title",
        "author",
        "tag",
        "time",
        "slug",
        "pub_date",
    )
    empty_value_display = "-пусто-"


admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
