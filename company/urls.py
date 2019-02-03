from django.urls import path
from . import views

urlpatterns = [
    path('', views.CompanyTable, name='company-table'),
    path('view/', views.CompanyView, name='company-view'),
]