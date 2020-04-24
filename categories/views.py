from django.shortcuts import render 
from products.models import Product

def do_categories(request):
    products = Product.objects.filter(categories__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})




