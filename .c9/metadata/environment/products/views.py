{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":7,"position":7,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.shortcuts import render","","# Create your views here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":6,"column":67},"action":"insert","lines":["from django.shortcuts import render","from .models import Product","","# Create your views here.","def all_products(request):","    products = Product.objects.all()","    return render(request, \"products.html\", {\"products\": products})"]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":25},"action":"remove","lines":["# Create your views here."],"id":3},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":4,"column":36},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":4},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["p"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["r"]},{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["i"]},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["n"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":[" "],"id":5},{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["p"]},{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["r"]},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["o"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":13},"action":"remove","lines":["pro"],"id":6},{"start":{"row":5,"column":10},"end":{"row":5,"column":18},"action":"insert","lines":["products"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":11},"action":"insert","lines":["("],"id":7}],[{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":[")"],"id":8}],[{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"remove","lines":[" "],"id":9}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":19},"end":{"row":5,"column":19},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588078283745,"hash":"faf8113b6a93c5ff5fad9c0cc4841502f7441e78"}