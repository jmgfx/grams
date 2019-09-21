from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetTable, name='asset-table'),
    path('view/<int:asset_id>/', views.AssetView, name='asset-view'),
    path('view/<int:asset_id>/use', views.InUse, name='in-use'),
    path('view/<int:asset_id>/store', views.Store, name='store'),
    path('view/<int:asset_id>/edit/', views.AssetEdit, name='asset-edit'),
    path('view/<int:asset_id>/depreciate/', views.Depreciate, name='depreciate-asset'),
    path('view/<int:asset_id>/revalue/', views.Revalue, name='asset-revalue'),
    path('view/<int:asset_id>/revalue/true/', views.RevalueAlgo, name='asset-revalue-true'),
    path('delete/<int:asset_id>', views.DeleteAsset, name='delete-asset'),
    path('add/', views.AssetAdd, name='asset-add'),
    path('archive/', views.ArchivedAssetsTable, name='archived-assets-table'),
    path('archive/<int:asset_id>/', views.AssetArchive, name='asset-archive'),
    path('recover/<int:asset_id>/', views.AssetRecover, name='asset-recover'),
]