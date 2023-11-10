from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.

@login_required
def index(request):
    #return HttpResponse('This is the index page')
    return render(request,'dashboard/index.html')

@login_required
def staff(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/staff.html')

@login_required
def product(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/product.html')

@login_required
def order(request):
    #return HttpResponse('This is the staff page')
    return render(request,'dashboard/order.html')