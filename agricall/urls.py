from django.urls import path
from . import views,CreateProduct

#URLconfiguration
urlpatterns = [
    path('agricall/', views.say_hello, name='say_hello'),
    path('store/', views.show_products, name='show_products'),
    path('create_product/',CreateProduct.as_view(),name='create_product'),
]
