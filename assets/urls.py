from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetTable, name='asset-table'),
    path('view/<int:asset_id>', views.AssetView, name='asset-view'),
    path('view/<int:asset_id>/edit/', views.AssetEdit, name='asset-edit'),
    path('view/<int:asset_id>/revalue/', views.Revalue, name='asset-revalue'),
    path('view/<int:asset_id>/revalue/true/', views.RevalueAlgo, name='asset-revalue-true'),
    path('add/', views.AssetAdd, name='asset-add'),
    path('archive/', views.ArchivedAssetsTable, name='archived-assets-table'),
    path('archive/<int:asset_id>/', views.AssetArchive, name='asset-archive'),
    path('recover/<int:asset_id>/', views.AssetRecover, name='asset-recover'),
]