from django.urls import path
from . import views

urlpatterns = [
    path('', views.VendorsTable, name='vendors-table'),
    path('view/', views.VendorsView, name='vendors-view'),
]