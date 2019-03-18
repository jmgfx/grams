from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Transactions
from .forms import MaintenanceForm, TransferForm, DisposeForm, RecoverForm
from .services import DefaultDescription

from assets.models import Assets


@login_required
def TransactionView(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)

    if transaction.ttype == '1':
        type = 'Maintenance'
    elif transaction.ttype == '2':
        type = 'Transfer'
    elif transaction.ttype == '3':
        type = 'Archived'
    elif transaction.ttype == '4':
        type = 'Recover'
    else:
        type = 'Transaction'

    context = {
        'transaction_view': Transactions.objects.get(id=transaction_id),
        'title': str(type+' ID#'+str(transaction_id)),
    }
    return render(request, 'transactionview.html', context)


@login_required
def TransactionsTable(request):
    context = {
        'transactions': Transactions.objects.all(),
    }
    return render(request, 'queue.html', context, {'title': 'Queued Transactions'})


@login_required
def TransactionsHistory(request):
    return HttpResponse('History of transactions goes here.')


@login_required
def Maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 1
            new_transaction.created_by = request.user

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = MaintenanceForm()
    return render(request, 'schedule.html', {'form': form}, {'title': 'Schedule Maintenance'})


@login_required
def Transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 2
            new_transaction.created_by = request.user

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
            
            return redirect('/transactions/transfer/' + str(new_transaction.id) + '/')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form}, {'title': 'Transfer Assets'})


@login_required
def TransferAction(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    for asset in transaction.assets_transact.all():
        asset_to_transfer = Assets.objects.get(id=asset.id)
        asset_to_transfer.branch = transaction.branch_destination
        asset_to_transfer.save()
    return redirect('/transactions/view/' + str(transaction_id) + '/')


@login_required
def Dispose(request):
    if request.method == 'POST':
        form = DisposeForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 3
            new_transaction.created_by = request.user

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()

            return redirect('/transactions/dispose/' + str(new_transaction.id) + '/')
    else:
        form = DisposeForm()
    return render(request, 'dispose.html', {'form': form}, {'title': 'Transfer Assets'})


@login_required
def DisposeAction(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    for asset in transaction.assets_transact.all():
        asset_to_archive = Assets.objects.get(id=asset.id)
        asset_to_archive.status = 'Archived'
        asset_to_archive.display = 0
        asset_to_archive.save()
    return redirect('/transactions/view/' + str(transaction_id) + '/')


@login_required
def Recover(request):
    if request.method == 'POST':
        form = RecoverForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 4
            new_transaction.created_by = request.user

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()

            return redirect('/transactions/recover/' + str(new_transaction.id) + '/')
    else:
        form = RecoverForm()
    return render(request, 'recover.html', {'form': form}, {'title': 'Transfer Assets'})


@login_required
def RecoverAction(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    for asset in transaction.archived_assets.all():
        asset_to_recover = Assets.objects.get(id=asset.id)
        asset_to_recover.status = 'In Storage'
        asset_to_recover.display = 1
        asset_to_recover.save()
    return redirect('/transactions/view/' + str(transaction_id) + '/')


def DefaultDescription(self):
    if self.ttype == 1:
        return 'Maintenance scheduled from ' + self.start_date.strftime('%B %d, %Y') + ' to ' + self.end_date.strftime('%B %d, %Y') + ' by ' + self.created_by + '.'
    elif self.ttype == 2:
        return 'Asset(s) transfered to ' + self.branch_destination.name + ' by ' + self.created_by + '.'
    elif self.ttype == 3:
        return 'Asset(s) were archived ' + ' by ' + self.created_by + '.'
    elif self.ttype == 4:
        return 'Asset(s) were recovered from the archive ' + ' by ' + self.created_by + '.'
    else:
        return 'Transaction set ' + ' by ' + self.created_by + '.'