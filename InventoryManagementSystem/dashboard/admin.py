from django.contrib import admin
from .models import Product,Order
from django.contrib.auth.models import Group


admin.site.site_header='Admin Management'
# admin.site.unregister(Group)
# Register your models here.

class productmanager(admin.ModelAdmin):
    list_display=('name','category','quantity')
    list_filter=('category','quantity')

# class ordermanager(admin.ModelAdmin):


admin.site.register(Product,productmanager)
admin.site.register(Order)