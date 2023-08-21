from django.shortcuts import render, redirect


def landing(request):
    return render(request,"landing.html")

def home(request):
    
    return render(request, 'home.html')


def contact(request):
    return render(request,"contact.html")

def result(request):
    
    return render(request,"result.html")