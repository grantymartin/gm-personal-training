from django import forms
from products.models import CATEGORIES


class CategoryForm(forms.Form):
    categories_field = forms.ChoiceField(
        choices = CATEGORIES
    )