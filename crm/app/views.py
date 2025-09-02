from django.shortcuts import render
from .models import AdminBored
# Create your views here.

def home(request):
    context = {}
    return render(request,'home.html',context)

def about(request):
    bored = AdminBored.objects.all()
    context = {'bored':bored}
    return render(request,'about.html',context)

def services(request):
    context = {}
    return render(request,'services.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)