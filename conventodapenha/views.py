from django.shortcuts import render

def home(request):
    return render(request, 'base.html')

def conhecaumpoucomais(request):
    return render(request, 'conventodapenha/index.html')
    
