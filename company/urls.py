from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyTable, name='company-table'),
    path('view/<int:company_id>', views.CompanyView, name='company-view'),
    path('view/<int:company_id>/edit/', views.CompanyEdit, name='company-edit'),
    path('add/', views.CompanyAdd, name='company-add'),
    path('archive/', views.CompanyArchive, name='company-archive')
]