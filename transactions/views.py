from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from .forms import MaintenanceForm


def TransactionsView(request):
    return HttpResponse('Transactions view goes here.')


def TransactionsTable(request):
    return HttpResponse('Transactions table goes here.')


def TransactionsHistory(request):
    return HttpResponse('History of transactions goes here.')


def Maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.save()
    else:
        form = MaintenanceForm()
    return render(request, 'schedule.html', {'form': form}, {'title': 'Schedule Maintenance'})
