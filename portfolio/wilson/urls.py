from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("landing/", views.landing, name="landing"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    
    
]
#path("<str:name>", views.greet, name="greet")