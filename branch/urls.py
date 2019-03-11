from django.urls import path
from . import views

urlpatterns = [
    path('', views.BranchTable, name='branch-table'),
    path('view/<int:branch_id>/', views.BranchView, name='branch-view'),
    path('view/<int:branch_id>/edit/', views.BranchEdit, name='branch-edit'),
    path('delete/<int:branch_id>/', views.DeleteBranch, name='delete-branch'),
    path('add/', views.BranchAdd, name='branch-add'),
    path('archive/', views.ArchivedBranchTable, name='branch-table-archive'),
    path('archive/<int:branch_id>', views.BranchArchive, name='branch-archive'),
    path('recover/<int:branch_id>', views.BranchRecover, name='branch-recover'),
]