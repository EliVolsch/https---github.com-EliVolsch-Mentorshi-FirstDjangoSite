from django.urls import path
from . import views

#URL Conf module for playground
urlpatterns = [
    path('', views.home),
    path('hello/', views.say_hello),
    path('viewmap/', views.turbines)
]
