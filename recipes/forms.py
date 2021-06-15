from django import forms

from .models import Recipe, Ingredient, RecipeIngredientRelation, Tag


class RecipeForm(forms.ModelForm):

    tag = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                         to_field_name='slug')

    class Meta:

        model = Recipe
        fields = ('title', 'time', 'description', 'tag',
                  'image',)


class IngredientsForm (forms.ModelForm):

    class Meta:

        model = RecipeIngredientRelation
        fields = ('ingredient', 'amount')
