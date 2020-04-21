from django.db import models
from django.forms import ModelForm
from products.models import CATEGORIES
class do_categories(models.Model):
    categories = models.CharField(max_length=3, choices=CATEGORIES)
    
   def __str__(self):
        return self.name

class categoriesForm(ModelForm):
    class Meta:
        model = do_categories
        fields = ['categories']



#class MyModelForm(ModelForm):
 #   class Meta:
 #       model = Product
  #      fields = ['CATEGORIES']