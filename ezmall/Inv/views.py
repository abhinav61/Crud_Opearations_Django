from django.shortcuts import render
from .models import Product,Order,Customer

# Create your views here. 

def dashboard(request):
    return render(request,'Inv/dashboard.html')

def product(request):
    item = Product.objects.all()
    
    return render(request,'Inv/product.html',{'items':item})

def customer(request):
    return render(request,'Inv/customer.html')
