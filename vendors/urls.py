from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorsTable, name='vendors-table'),
    path('view/<int:vendor_id>/', views.VendorsView, name='vendors-view'),
    path('view/<int:vendor_id>/edit/', views.VendorsEdit, name='vendors-edit'),
    path('add/', views.VendorsAdd, name='vendors-add'),
    path('archive/', views.VendorsArchive, name='vendors-archive'),
]