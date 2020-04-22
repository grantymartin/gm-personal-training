from django.shortcuts import render 
from products.models import Product
from .forms import  CategoryForm

def do_categories(request):
    products = Product.objects.filter(categories__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})

#def categories(request): 
#    context = {} 
#    form = CategoryForm()
#   context['form'] = form
#    if request.GET:
#        temp = request.GET['categories_field']
#        print(temp)
#    
#    return render( request, "products.html", context)




