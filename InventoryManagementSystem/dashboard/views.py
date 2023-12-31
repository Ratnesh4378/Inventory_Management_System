from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
import matplotlib.pyplot as plt
import base64
from io import BytesIO
# Create your views here.

#view for the main dashboard page
@login_required
def index(request):
    most_recent_entry = Order.objects.latest('date')
    recent_name=most_recent_entry.staff.username
    order_count = Order.objects.count() 
    product_count = Product.objects.count() 
    users_count= User.objects.count()
    #plotting pie chart for the orders
    orders=Order.objects.all()
    products=Product.objects.all()
    labels=[order.product.name for order in orders]
    data = [order.quantity for order in orders]
    plt.figure(figsize=(6, 6))
    wedges, texts, autotexts=plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Orders',fontsize=16)
    plt.legend(wedges, labels, title="Products",loc="center left",bbox_to_anchor=(-0.1, 1))
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    pie_chart = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

    #plotting bar graph for the roducts
    labels = [product.name for product in products]
    data = [product.quantity for product in products]
    plt.figure(figsize=(8, 6))
    bars=plt.bar(labels, data, color=plt.cm.Paired.colors)
    plt.legend(bars, labels, loc='upper left')
    plt.title('Products',fontsize=16)
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    bar_graph = base64.b64encode(buffer.read()).decode('utf-8')
    buffer.close()

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
        'pie_chart': pie_chart,
        'bar_graph': bar_graph,
        'order_count': order_count,
        'product_count': product_count,
        'users_count' : users_count,
        'recent_name': recent_name,
    }
    return render(request,'dashboard/index.html',context)

#view for the staff page
@login_required
def staff(request):
    most_recent_entry = Order.objects.latest('date')
    recent_name=most_recent_entry.staff.username
    order_count = Order.objects.count() 
    product_count = Product.objects.count() 
    users_count= User.objects.count()
    workers=User.objects.all()
    context={
        'workers':workers,
        'order_count':order_count,
        'product_count': product_count,
        'users_count' : users_count,
        'recent_name': recent_name,
    }
    return render(request,'dashboard/staff.html',context)

#view for the staff_details page , as and when the admin will click on view button
@login_required
def staff_detail(request,primaryKey):
    most_recent_entry = Order.objects.latest('date')
    recent_name=most_recent_entry.staff.username
    order_count = Order.objects.count() 
    product_count = Product.objects.count() 
    users_count= User.objects.count()
    
    workers=User.objects.get(id=primaryKey)
    context={
        'workers':workers,
        'order_count':order_count,
        'product_count': product_count,
        'users_count' : users_count,
        'recent_name': recent_name,
    }
    return render(request,'dashboard/staff_detail.html',context)

#view for the product page
@login_required
def product(request):
    #return HttpResponse('This is the staff page')
    #items=Product.objects.all()
    most_recent_entry = Order.objects.latest('date')
    recent_name=most_recent_entry.staff.username
    order_count = Order.objects.count() 
    product_count = Product.objects.count() 
    users_count= User.objects.count()
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
        'order_count':order_count,
        'product_count': product_count,
        'users_count' : users_count,
        'recent_name': recent_name,
    }
    return render(request,'dashboard/product.html',context)

#view for the order page
@login_required
def order(request):
    #return HttpResponse('This is the staff page')
    most_recent_entry = Order.objects.latest('date')
    recent_name=most_recent_entry.staff.username
    order_count = Order.objects.count() 
    product_count = Product.objects.count() 
    users_count= User.objects.count()
    orders=Order.objects.all()
    context={
        'orders':orders,
        'order_count':order_count,
        'product_count': product_count,
        'users_count' : users_count,
        'recent_name': recent_name,
    }
    return render(request,'dashboard/order.html',context)

#view for the product delete page
@login_required
def product_delete(request,primaryKey):
    item= Product.objects.get(id=primaryKey)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/product_delete.html')

#view for the product update page
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