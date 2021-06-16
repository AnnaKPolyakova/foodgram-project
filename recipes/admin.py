from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin

from recipes.models import Tag, Ingredient, Recipe, RecipeIngredientRelation, \
    Follow


class RecipeIngredientLine(SortableInlineAdminMixin, admin.TabularInline):
    model = RecipeIngredientRelation
    verbose_name_plural = 'Доп. информация'


class TegAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    search_fields = ('title', 'slug',)
    empty_value_display = '-пусто-'


class MeasureAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    empty_value_display = '-пусто-'


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', 'measure',)
    search_fields = ('title', 'measure',)
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    filter_horizontal = ('tag',)
    inlines = (RecipeIngredientLine,)
    list_display = ('title', 'author', 'time', 'pub_date',)
    search_fields = ('title', 'author', 'tag', 'time', 'slug', 'pub_date',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('user', 'author',)
    search_fields = ('user', 'author',)
    empty_value_display = '-пусто-'


admin.site.register(Follow, FollowAdmin)
admin.site.register(Tag, TegAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)

