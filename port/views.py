from django.shortcuts import render

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