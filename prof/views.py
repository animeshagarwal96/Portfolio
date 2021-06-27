from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'portfolio/home.html')

def business(request):
    return render(request,'portfolio/business.html')

def resume(request):
    return render(request,'portfolio/resume.html')

def contact(request):
    return render(request,'portfolio/contact.html')

def about(request):
    return render(request,'portfolio/about.html')
