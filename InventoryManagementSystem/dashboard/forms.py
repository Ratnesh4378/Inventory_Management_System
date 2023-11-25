from django import forms
from .models import Product,Order

#form for the entry of new product by admin
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name','category','quantity']

#form for the new order by the staff
class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields=['product','quantity']
