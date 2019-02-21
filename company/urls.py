from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyTable, name='company-table'),
    path('view/', views.CompanyView, name='company-view'),
    path('add/', views.CompanyAdd, name='company-add'),
    path('edit/', views.CompanyEdit, name='company-edit'),
    path('archive/', views.CompanyArchive, name='company-archive')
]