from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),

    path("home",views.home,name="home"),

    path("post",views.post,name="post_page"),
    
    path("post/<slug:slug>",views.post_detail,name="post_details_page"),

    path("about",views.about,name="about"),

    path("service",views.service,name="service"),

    path("skill",views.skill,name="skill"),

    path("contact",views.contact,name="contact")
]



