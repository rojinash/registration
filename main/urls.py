from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register), #not somewhere you can go, just processes your registration form
    path('login', views.login),
    path('post_blogs', views.post_blogs),
    path('logout', views.logout),
    path('process_blog', views.process_blog),
    path('homepage', views.homepage),
]