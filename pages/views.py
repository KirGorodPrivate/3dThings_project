from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def services(request):
    return render(request, 'pages/services.html')

def materials(request):
    return render(request, 'pages/materials.html')

def design(request):
    return render(request, 'pages/design.html')