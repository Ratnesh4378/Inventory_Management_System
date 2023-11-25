from django.db import models
from django.contrib.auth.models import Group,User

#The categories of products are stored in this 
availableCategories=(('Food','Food'),
('Clothes','Clothes'),
('Stationary','Stationary')
)

#schema for the Product Table
class Product(models.Model):
    name=models.CharField(max_length=40,null=True)
    category=models.CharField(max_length=20,choices=availableCategories,null=True)
    quantity=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural='Product'

    def __str__(self):
        return f'{self.name}   {self.category}    {self.quantity}'

#schema for the Order table
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    quantity=models.PositiveIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Order'
    
    def __str__(self):
        return f'{self.product}  ordered by {self.staff.username}'