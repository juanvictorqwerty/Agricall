from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request handler part

def welcome_user(request):
    return render(request,'index.html')
