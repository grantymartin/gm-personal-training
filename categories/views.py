from django import forms
from products.models import CATEGORIES

class CategoryForm(forms.Form):
    categories = forms.CharField(
        widget=forms.Select(choices=CATEGORIES),
    )







#from django.forms import ModelForm
#from products.models import Product
#from categories.forms import MyModelForm
#from django.shortcuts import render
#
#def CreateMyModelView(CreateView):
 #   model = Product
 #   form_class = MyModelForm
 #   return render(Product, "products.html", {"form_class": form_class})