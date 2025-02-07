from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
    path('agricall/', views.say_hello, name='say_hello'),
]