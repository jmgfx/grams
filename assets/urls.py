from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssetTable, name='asset-table'),
    path('view/', views.AssetView, name='asset-view'),
]