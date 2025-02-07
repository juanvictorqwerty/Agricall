from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
    path('', views.say_hello, name='say_hello'),
]