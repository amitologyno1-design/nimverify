from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def register(request):
    return render(request, 'home/register.html')