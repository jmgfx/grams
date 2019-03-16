from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsTable, name='transactions-table'),
    path('maintenance/', views.Maintenance, name='schedule-maintenance'),
    path('transfer/', views.Transfer, name='transfer-asset'),
    path('dispose/', views.Dispose, name='dispose-asset'),
    path('dispose/<int:transaction_id>/', views.DisposeAction, name='dispose-asset-action'),
    path('recover/', views.Recover, name='recover-asset'),
    path('recover/<int:transaction_id>/', views.RecoverAction, name='recover-asset-action'),
    path('history/', views.TransactionsHistory, name='transactions-history'),
    path('view/dispose/<int:transaction_id>/', views.DisposeView, name='dispose-transaction-view'),
    path('view/recover/<int:transaction_id>/', views.DisposeView, name='dispose-transaction-view'),
]