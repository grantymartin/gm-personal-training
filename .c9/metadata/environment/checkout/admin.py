{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":3,"position":3,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.contrib import admin","","# Register your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":12,"column":38},"action":"insert","lines":["from django.contrib import admin","from .models import Order, OrderLineItem","","","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","","","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","","","admin.site.register(Order, OrderAdmin)"]}],[{"start":{"row":1,"column":40},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":4,"column":25},"end":{"row":5,"column":0},"action":"remove","lines":["",""],"id":4}],[{"start":{"row":7,"column":38},"end":{"row":8,"column":0},"action":"remove","lines":["",""],"id":5}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":38},"end":{"row":7,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1588161702179,"hash":"d1ee12ee885cddf7c6bdcd7d5127d2299dbb33f0"}