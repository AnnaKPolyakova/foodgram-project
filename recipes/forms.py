from django import forms

from .models import Recipe, Tag


class RecipeForm(forms.ModelForm):

    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), to_field_name="slug"
    )

    class Meta:

        model = Recipe
        fields = (
            "title",
            "time",
            "description",
            "tags",
            "image",
        )
