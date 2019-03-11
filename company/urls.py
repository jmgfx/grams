from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyTable, name='company-table'),
    path('view/<int:company_id>/', views.CompanyView, name='company-view'),
    path('view/<int:company_id>/edit/', views.CompanyEdit, name='company-edit'),
    path('delete/<int:company_id>/', views.DeleteCompany, name='delete-company'),
    path('recover/<int:company_id>/', views.RecoverCompany, name='recover-company'),
    path('add/', views.CompanyAdd, name='company-add'),
    path('archive/', views.ArchivedCompanyTable, name='archive-company-table'),
    path('archive/<int:company_id>/', views.ArchiveCompany, name='archive-company'),
]