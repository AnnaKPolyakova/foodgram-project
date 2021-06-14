from django import forms

from .models import Recipe, Ingredient, RecipeIngredientRelation, Tag


class RecipeForm(forms.ModelForm):

    class Meta:

        model = Recipe
        fields = ('title', 'time', 'description',
                  'image', )
    #
    # widgets = {
    #     'tag': forms.CheckboxSelectMultiple()
    # }


class IngredientsForm (forms.ModelForm):

    class Meta:

        model = RecipeIngredientRelation
        fields = ('ingredient', 'amount')
