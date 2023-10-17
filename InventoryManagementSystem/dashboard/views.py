from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('This is the index page')
    return render(request,'dashboard/index.html')

def staff(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/staff.html')

def product(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/product.html')

def order(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/order.html')