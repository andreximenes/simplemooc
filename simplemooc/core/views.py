from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request, 'home.html', {'usuario': 'André Ximenes', })

def login(request):
    return render(request, 'login.html', {})

def contato(request):
    return render(request, 'contato.html', {})
