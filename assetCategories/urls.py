from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetCategoriesTable, name='asset-categories-table'),
    path('view/<int:category_id>', views.AssetCategoriesView, name='asset-categories-view'),
    path('view/<int:category_id>/edit/', views.AssetCategoriesEdit, name='asset-categories-edit'),
    path('add/', views.AssetCategoriesAdd, name='asset-categories-add'),
    path('archive/', views.AssetCategoriesArchive, name='asset-categories-archive'),
]