from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Transactions
from .forms import MaintenanceForm, TransferForm, DisposeForm, RecoverForm, DefectiveForm
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
        'transactions': Transactions.objects.filter(status=1),
        'title': 'Queued Transactions',
    }
    return render(request, 'queue.html', context)


@login_required
def TransactionsHistory(request):
    context = {
        'transactions': Transactions.objects.filter(status=2),
        'title': 'Queued Transactions',
    }
    return render(request, 'history.html', context)


@login_required
def Maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 1
            new_transaction.created_by = request.user
            new_transaction.status = 1

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
    else:
        form = MaintenanceForm()

    context = {
        'form': form,
        'title': 'Schedule Maintenance Assets',
    }
    return render(request, 'schedule.html', {'form': form}, {'title': 'Schedule Maintenance'})


@login_required
def Transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 2
            new_transaction.created_by = request.user
            new_transaction.status = 2

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()
            
            return redirect('/transactions/transfer/' + str(new_transaction.id) + '/')
    else:
        form = TransferForm()

    context = {
        'form': form,
        'title': 'Transfer Assets',
    }
    return render(request, 'transfer.html', context)


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
            new_transaction.status = 2

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()

            return redirect('/transactions/dispose/' + str(new_transaction.id) + '/')
    else:
        form = DisposeForm()

    context = {
        'form': form,
        'title': 'Dispose/Archive Assets',
    }
    return render(request, 'dispose.html', context)


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
            new_transaction.status = 2

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()

            return redirect('/transactions/recover/' + str(new_transaction.id) + '/')
    else:
        form = RecoverForm()

    context = {
        'form': form,
        'title': 'Recover Archived Assets',
    }
    return render(request, 'recover.html', context)


@login_required
def RecoverAction(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    for asset in transaction.archived_assets.all():
        asset_to_recover = Assets.objects.get(id=asset.id)
        asset_to_recover.status = 'In Storage'
        asset_to_recover.display = 1
        asset_to_recover.save()
    return redirect('/transactions/view/' + str(transaction_id) + '/')


@login_required
def Defective(request):
    if request.method == 'POST':
        form = DefectiveForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.ttype = 5
            new_transaction.created_by = request.user
            new_transaction.status = 2

            new_transaction.description = DefaultDescription(new_transaction)

            new_transaction.save()
            form.save_m2m()

            return redirect('/transactions/defective/' + str(new_transaction.id) + '/')
    else:
        form = DefectiveForm()

    context = {
        'form': form,
        'title': 'Report Defective Assets',
    }
    return render(request, 'defective.html', context)


@login_required
def DefectiveAction(request, transaction_id):
    transaction = Transactions.objects.get(id=transaction_id)
    for asset in transaction.assets_transact.all():
        asset_to_recover = Assets.objects.get(id=asset.id)
        asset_to_recover.status = 'Defective'
        asset_to_recover.display = 1
        asset_to_recover.save()
    return redirect('/transactions/view/' + str(transaction_id) + '/')


def DefaultDescription(self):
    if self.ttype == 1:
        return 'Maintenance scheduled on ' + self.start_date.strftime('%B %d, %Y') + ' by ' + str(self.created_by) + '.'
    elif self.ttype == 2:
        return 'Asset(s) transfered to ' + self.branch_destination.name + ' by ' + str(self.created_by) + '.'
    elif self.ttype == 3:
        return 'Asset(s) were archived by ' + str(self.created_by) + '.'
    elif self.ttype == 4:
        return 'Asset(s) were recovered from the archive by ' + str(self.created_by) + '.'
    elif self.ttype == 5:
        return 'Asset(s) were reported defective by ' + str(self.created_by) + '.'
    else:
        return 'Transaction set ' + ' by ' + str(self.created_by) + '.'