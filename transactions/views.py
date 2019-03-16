from django.shortcuts import render
from django.http import HttpResponse
from .models import Transactions
from .forms import MaintenanceForm, TransferForm, DisposeForm, RecoverForm
from .services import DefaultDescription


def TransactionsView(request, type, transaction_id):
    return HttpResponse('Transactions view goes here.')


def TransactionsTable(request):
    context = {
        'transactions': Transactions.objects.all(),
    }
    return render(request, 'queue.html', context, {'title': 'Queued Transactions'})


def TransactionsHistory(request):
    return HttpResponse('History of transactions goes here.')


def Maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 1

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = MaintenanceForm()
    return render(request, 'schedule.html', {'form': form}, {'title': 'Schedule Maintenance'})


def Transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 2

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form}, {'title': 'Transfer Assets'})


def Dispose(request):
    if request.method == 'POST':
        form = DisposeForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 3

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = DisposeForm()
    return render(request, 'dispose.html', {'form': form}, {'title': 'Transfer Assets'})


def Recover(request):
    if request.method == 'POST':
        form = RecoverForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 4

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = RecoverForm()
    return render(request, 'recover.html', {'form': form}, {'title': 'Transfer Assets'})


def DefaultDescription(self):
    if self.ttype == 1:
        return 'Maintenance scheduled from ' + self.start_date.strftime('%B %d, %Y') + ' to ' + self.end_date.strftime('%B %d, %Y') + '.'
    elif self.ttype == 2:
        return 'Asset(s) transfered to ' + self.branch_destination.name + '.'
    elif self.ttype == 3:
        return 'Asset(s) were archived.'
    elif self.ttype == 4:
        return 'Asset(s) were recovered from the archive.'
    else:
        return 'Transaction set.'