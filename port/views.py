from django.shortcuts import render
from .models import form
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,"port/index.html")

def post(request):
    pass

def post_detail(request):
    pass

def about(request):
    return render(request,"port/about.html")

def service(request):
    return render(request,"port/service.html")


def skill(request):
    return render(request, "port/skill.html")


def contact(request):
    return render(request, "port/contact.html")

def insert_data(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        describe=request.POST['describe']
        my= form(name=name,email=email,subject=subject,describe=describe)
        my.save()
        return render(request,"port/contact.html")
    else:
        return render(request,"port/contact.html")


    