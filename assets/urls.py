from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetTable, name='asset-table'),
    path('view/', views.AssetView, name='asset-view'),
    path('add/', views.AssetAdd, name='asset-add'),
    path('edit/', views.AssetEdit, name='asset-edit'),
    path('archive/', views.AssetArchive, name='asset-archive'),
]