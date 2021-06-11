from django import forms

from .models import Recipe, Ingredient, RecipeIngredientRelation


class RecipeForm(forms.ModelForm):

    class Meta:

        model = Recipe
        fields = ('title', 'tag', 'time', 'description',
                  'image', 'slug', )
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }


class IngredientsForm (forms.ModelForm):

    class Meta:

        model = RecipeIngredientRelation
        fields = ('ingredient', 'amount')
