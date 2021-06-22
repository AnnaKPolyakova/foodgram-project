from django import forms

from .models import Ingredient, Recipe, RecipeIngredientRelation, Tag


class RecipeForm(forms.ModelForm):

    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                         to_field_name='slug')

    class Meta:

        model = Recipe
        fields = ('title', 'time', 'description', 'tag',
                  'image',)
