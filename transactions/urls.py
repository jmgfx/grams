from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsTable, name='transactions-table'),
    path('maintenance/', views.Maintenance, name='schedule-maintenance'),
    path('transfer/', views.Transfer, name='transfer-asset'),
    path('dispose/', views.Dispose, name='dispose-asset'),
    path('recover/', views.Recover, name='recover-asset'),
    path('history/', views.TransactionsHistory, name='transactions-history'),
    path('view/<int:type>/<int:transaction_id>/', views.TransactionsView, name='transaction-view'),
]