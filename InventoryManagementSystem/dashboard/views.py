from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    #return HttpResponse('This is the index page')
    orders=Order.objects.all()
    products=Product.objects.all()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()
    context={
        'orders':orders,
        'form':form,
        'products':products,
    }
    return render(request,'dashboard/index.html',context)

@login_required
def staff(request):
    #return HttpResponse('This is the staff page')
    workers=User.objects.all()
    context={
        'workers':workers,
    }
    return render(request,'dashboard/staff.html',context)

@login_required
def staff_detail(request,primaryKey):
    workers=User.objects.get(id=primaryKey)
    context={
        'workers':workers,
    }
    return render(request,'dashboard/staff_detail.html',context)

@login_required
def product(request):
    #return HttpResponse('This is the staff page')
    #items=Product.objects.all()

    items=Product.objects.raw('SELECT * FROM dashboard_product')
    if request.method=='POST':
        form= ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
        
            return redirect('dashboard-product')
    else:
        form=ProductForm()

    context={
        'items':items,
        'form':form,
    }
    return render(request,'dashboard/product.html',context)

@login_required
def order(request):
    #return HttpResponse('This is the staff page')
    orders=Order.objects.all()
    context={
        'orders':orders,
    }
    return render(request,'dashboard/order.html',context)

@login_required
def product_delete(request,primaryKey):
    item= Product.objects.get(id=primaryKey)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

@login_required
def product_update(request,primaryKey):
    item= Product.objects.get(id=primaryKey)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)
    context={
        'form':form,
    }
    return render(request,'dashboard/product_update.html',context)