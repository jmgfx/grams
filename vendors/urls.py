from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorsTable, name='vendors-table'),
    path('view/', views.VendorsView, name='vendors-view'),
    path('add/', views.VendorsAdd, name='vendors-add'),
    path('edit/', views.VendorsEdit, name='vendors-edit'),
    path('archive/', views.VendorsArchive, name='vendors-archive'),
]