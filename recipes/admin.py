from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin

from recipes.models import Teg, Measure, Ingredient, Recipe, RecipeIngredientRelation


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
    filter_horizontal = ('teg',)
    inlines = (RecipeIngredientLine,)
    list_display = ('title', 'author', 'time', 'slug', 'pub_date',)
    search_fields = ('title', 'author', 'teg', 'time', 'slug', 'pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Teg, TegAdmin)
admin.site.register(Measure, MeasureAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)

