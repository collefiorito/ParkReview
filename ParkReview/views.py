# filepath: c:\django\ParkReview\ParkReview\views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def mappa(request):
    return render(request, 'mappa.html')

def recensioni(request):
    return render(request, 'recensioni.html')

def about(request):
    return render(request, 'about.html')