from django import forms

from .models import Recipe, Ingredient, RecipeIngredientRelation, Tag


class RecipeForm(forms.ModelForm):

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())

    class Meta:

        model = Recipe
        fields = ('title', 'tags', 'time', 'description',
                  'image', 'slug', )


class IngredientsForm (forms.ModelForm):

    class Meta:

        model = RecipeIngredientRelation
        fields = ('ingredient', 'amount')
