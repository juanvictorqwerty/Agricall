from django.shortcuts import render
from django.http import HttpResponse

from agricall.models import Products
from django.views import View
from .forms import ProductForm

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

#class CreateProduct(View):

#    def get(self ,request,*args,**kwargs):
#        return render(request,'Folders/create_product.html')
#    def post(self,request,*args,**kwargs):
#        name = request.POST.get('name')
#        description = request.POST.get('description')
#        price = request.POST.get('price')
#       image = request.FILES.get('image')

#        products = Products.objects.create(name=name ,description=description ,price=price,image=image)
#        products.save()

#        return HttpResponse("Product successfully inserted")

class CreateProduct(View):
    def get(self,request,*args,**kwargs):
        form = ProductForm()
        return render (request,"Folders/create_product.html",{'form':form})
    
    def post(self,request,*args,**kwargs):
        form = ProductForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponse('Product successfully stored')
        else:
            return render(request,'Folders/create_product.html',{'form':form})