from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsTable, name='transactions-table'),
    path('maintenance/', views.Maintenance, name='schedule-maintenance'),
    path('transfer/', views.Transfer, name='transfer-asset'),
    path('transfer/<int:transaction_id>/', views.TransferAction, name='dispose-asset-action'),
    path('dispose/', views.Dispose, name='dispose-asset'),
    path('dispose/<int:transaction_id>/', views.DisposeAction, name='dispose-asset-action'),
    path('recover/', views.Recover, name='recover-asset'),
    path('recover/<int:transaction_id>/', views.RecoverAction, name='recover-asset-action'),
    path('defective/', views.Defective, name='defective-asset'),
    path('defective/<int:transaction_id>/', views.DefectiveAction, name='defective-asset-action'),
    path('history/', views.TransactionsHistory, name='transactions-history'),
    path('view/<int:transaction_id>/', views.TransactionView, name='transaction-view'),
    path('view/<int:transaction_id>/close', views.CloseTransaction, name='close-transaction'),
    path('view/<int:transaction_id>/open', views.OpenTransaction, name='open-transaction'),
    path('view/<int:transaction_id>/delete', views.DeleteTransaction, name='delete-transaction'),
]