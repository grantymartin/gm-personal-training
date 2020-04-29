from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from classes.forms import Email_form

def email(request):
    if request.method == "POST":
        get_email = Email_form(request.POST)
        
        if get_email.is_valid():
            
            return HttpResponseRedirect('/submitted/')

    else:
        get_email = Email_form()

    return render(request, 'classes.html', {'get_email': get_email})
