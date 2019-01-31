from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsTable, name='transactions-table'),
    path('view/', views.TransactionsView, name='transactions-view'),
]