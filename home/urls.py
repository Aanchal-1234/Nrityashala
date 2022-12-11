from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("classes", views.classes, name='classes'),
    path("signup", views.signup, name='signup'),
    path("contact", views.contact, name='contact'),
]