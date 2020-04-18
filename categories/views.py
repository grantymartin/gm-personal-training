from django.shortcuts import render
from products.models import Product

# Create your views here.
def do_categories(request):
    products = Product.objects.filter(name__icontains=request.GET['x'])
    return render(request, "products.html", {"products": products})