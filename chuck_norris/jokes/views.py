from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse(


"<form action='http://api.icndb.com/jokes/random?'+firstName'&'+lastName'>"
"First name: <input type='text' name='firstName' value='Mickey'><br>"
"Last name: <input type='text' name='lastName' value='Mouse'><br>"
"<input type='submit' value='Submit'>"
"</form>"

    )
