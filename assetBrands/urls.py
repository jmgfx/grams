from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetBrandsTable, name='asset-brands-table'),
    path('view/<int:brand_id>', views.AssetBrandsView, name='asset-brands-view'),
    path('view/<int:brand_id>/edit/', views.AssetBrandsEdit, name='asset-brands-edit'),
    path('add/', views.AssetBrandsAdd, name='asset-brands-add'),
    path('archive/', views.AssetBrandsArchive, name='asset-brands-archive'),
]