from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register), #not somewhere you can go, just processes your registration form
    path('login', views.login),
    path('welcome', views.welcome),
]