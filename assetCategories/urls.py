from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetCategoriesTable, name='asset-categories-table'),
    path('view/<int:category_id>', views.AssetCategoriesView, name='asset-categories-view'),
    path('add/', views.AssetCategoriesAdd, name='asset-categories-add'),
    path('edit/', views.AssetCategoriesEdit, name='asset-categories-edit'),
    path('archive/', views.AssetCategoriesArchive, name='asset-categories-archive'),
]