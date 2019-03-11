from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsTable, name='transactions-table'),
    path('maintenance/', views.Maintenance, name='schedule-maintenance'),
    path('transfer/', views.Transfer, name='transfer-asset'),
    path('view/', views.TransactionsView, name='transactions-view'),
    path('history/', views.TransactionsHistory, name='transactions-history'),
]