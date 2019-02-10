from django.urls import path
from . import views

urlpatterns = [
    path('', views.BranchTable, name='branch-table'),
    path('view/', views.BranchView, name='branch-view'),
    path('add/', views.BranchAdd, name='branch-add'),
    path('edit/', views.BranchEdit, name='branch-edit'),
    path('archive/', views.BranchArchive, name='branch-archive'),
]