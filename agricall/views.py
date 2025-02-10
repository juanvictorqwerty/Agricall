from django.shortcuts import render
from django.http import HttpResponse

from agricall.models import Products

# Create your views here.
#request handler part

def welcome_user(request):
    return render(request,'index.html')

def show_products(request):
    products_list = Products.objects.all()
    context = {
    
        'products': products_list

    }
    return render(request,'store.html',context)