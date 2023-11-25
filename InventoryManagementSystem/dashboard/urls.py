from django.urls import path
from . import views

#URLS for dashboard, staff, staff-details, product, order, product-delete and product-update pages
urlpatterns=[
    path('dashboard/',views.index,name='dashboard-index'),
    path('staff/',views.staff,name='dashboard-staff'),
    path('staff/detail/<int:primaryKey>/',views.staff_detail,name='dashboard-staff-detail'),
    path('product/',views.product,name='dashboard-product'),
    path('order/',views.order,name='dashboard-order'),
    path('product/delete/<int:primaryKey>/',views.product_delete,name='dashboard-product-delete'),
    path('product/update/<int:primaryKey>/',views.product_update,name='dashboard-product-update'),
]