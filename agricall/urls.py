from django.urls import path
from . import views

#URLconfiguration
urlpatterns = [
    path('agricall/', views.say_hello, name='say_hello'),
    path('store/', views.show_products, name='show_products'),
]
