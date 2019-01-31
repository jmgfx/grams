from django.urls import path
from . import views

urlpatterns = [
    path('', views.BranchTable, name='branch-table'),
    path('view/', views.BranchView, name='branch-view'),
]