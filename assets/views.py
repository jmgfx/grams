from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.http import HttpResponse
from .models import Assets
from .forms import AddAssetForm, EditAssetForm, RevalueForm
from transactions.models import Transactions
from .services import GetDepreciation
from . import urls

import datetime
from datetime import date, timedelta


@login_required
def AssetTable(request):
    context = {
        'assets': Assets.objects.filter(display=1)
    }
    return render(request, 'assettable.html', context, {'title': 'Assets'})


@login_required
def AssetAdd(request):
    if request.method == 'POST':
        form = AddAssetForm(request.POST)
        if form.is_valid():
            new_asset = form.save(commit=False)

            new_asset.created_by = request.user

            # Whether to display asset in table or not
            if new_asset.status == 'Archived':
                new_asset.display = 0
            else:
                new_asset.display = 1

            # Compute depreciation hahahha sira toh
            new_asset.counter = new_asset.project_life
            new_asset.dep_value = (new_asset.acquisition_cost - new_asset.salvage_value) / new_asset.project_life
            new_asset.balance = new_asset.acquisition_cost

            new_asset.it_dep_value = []
            new_asset.it_dep_date = []
            new_asset.it_accrued = []
            new_asset.it_balance = []

            new_asset.it_dep_value.append(new_asset.dep_value)
            new_asset.it_dep_date.append(new_asset.date_acquired)
            new_asset.it_accrued.append(float(0.00))
            new_asset.it_balance.append(new_asset.acquisition_cost)

            # Save
            new_asset.save()
            return redirect('/assets/view/' + str(new_asset.id))
    else:
        form = AddAssetForm()

    context = {
        'form': form,
        'title': 'Add an Asset',
    }
    return render(request, 'addasset.html', context)


@login_required
def AssetView(request, asset_id):
    asset = Assets.objects.get(id=asset_id)
    now = datetime.date.today()

    asset.balance = asset.it_balance[-1]
    
    asset.save()

    dep_values = zip(asset.it_dep_date, asset.it_dep_value, asset.it_accrued, asset.it_balance)

    context_view = {
        'asset_view': asset,
        'audit_trail': Transactions.objects.filter(assets_transact__id__contains=asset_id).order_by('date_added'),
        'dep_values': dep_values,
        'title': asset.name,
    }

    return render(request, 'assetview.html', context_view)


@login_required
def InUse(request, asset_id):
    asset = Assets.objects.get(id=asset_id)
    asset.status = 'Use'
    asset.save()
    return redirect('/assets/view/' + str(asset_id) + '/')


@login_required
def Store(request, asset_id):
    asset = Assets.objects.get(id=asset_id)
    asset.status = 'Storage'
    asset.save()
    return redirect('/assets/view/' + str(asset_id) + '/')


@login_required
def AssetEdit(request, asset_id):
    if request.method == 'POST':
        form = EditAssetForm(request.POST, instance=Assets.objects.all().get(id=asset_id))
        if form.is_valid():
            form.save()
            return redirect('/assets/view/' + str(asset_id))
    else:
        form = EditAssetForm(instance=Assets.objects.all().get(id=asset_id))

    context = {
        'form': form,
        'asset': Assets.objects.get(id=asset_id),
        'title': 'Edit an Asset',
    }
    return render(request, 'editasset.html', context)


@login_required
def Revalue(request, asset_id):
    if request.method == 'POST':
        form = RevalueForm(request.POST, instance=Assets.objects.all().get(id=asset_id))
        if form.is_valid():
            form.save()
            return redirect('/assets/view/' + str(asset_id) + '/revalue/true/')
    else:
        form = RevalueForm(instance=Assets.objects.all().get(id=asset_id))
        
    context = {
        'form': form,
        'asset': Assets.objects.get(id=asset_id),
        'title': 'Revalue an Asset',
    }
    return render(request, 'revalue.html', context)


@login_required
def RevalueAlgo(request, asset_id):
    asset_to_revalue = Assets.objects.get(id=asset_id)
    asset_to_revalue.balance = asset_to_revalue.acquisition_cost
    asset_to_revalue.counter = asset_to_revalue.project_life
    asset_to_revalue.dep_value = (asset_to_revalue.acquisition_cost - asset_to_revalue.salvage_value) / asset_to_revalue.project_life

    asset_to_revalue.save()
    return redirect('/assets/view/' + str(asset_id))


@login_required
def AssetArchive(request, asset_id):
    asset_to_archive = Assets.objects.get(id=asset_id)
    asset_to_archive.status = 'Archived'
    asset_to_archive.display = 0
    asset_to_archive.save()
    return redirect('/assets/view/' + str(asset_id))


@login_required
def AssetRecover(request, asset_id):
    asset_to_recover = Assets.objects.get(id=asset_id)
    asset_to_recover.status = 'In Storage'
    asset_to_recover.display = 1
    asset_to_recover.save()
    return redirect('/assets/view/' + str(asset_id))


@login_required
def ArchivedAssetsTable(request):
    context = {
        'assets': Assets.objects.filter(display=0),
        'title': 'Archived Assets',
    }
    return render(request, 'assettablearchive.html', context)


@login_required
def DeleteAsset(request, asset_id):
    asset_to_delete = Assets.objects.get(id=asset_id)
    asset_to_delete.delete()
    return redirect('/assets/')


@login_required
def Depreciate(request, asset_id):
    asset = Assets.objects.get(id=asset_id)
    action = Depreciation(asset)
    asset.save()
    return redirect('/assets/view/' + str(asset_id) + '/')


def Depreciation(self):
    now = datetime.date.today()

    if now != get_last_day(now):
        last = get_prev_month(now)
        current_dep_date = get_last_day(last)
        gap = get_gap(self.it_dep_date[-1], current_dep_date)

        if self.it_dep_date[-1] > current_dep_date:
            zip_list = zip(self.it_dep_date, self.it_dep_value, self.it_accrued, self.it_balance)
            return zip_list

        elif self.date_added < current_dep_date:
            zip_list = zip(self.it_dep_date, self.it_dep_value, self.it_accrued, self.it_balance)
            return zip_list
            
        elif self.it_dep_date[-1] == current_dep_date:
            zip_list = zip(self.it_dep_date, self.it_dep_value, self.it_accrued, self.it_balance)
            return zip_list

        else:
            gap = get_gap(self.it_dep_date[-1], current_dep_date)

            while self.it_dep_date[-1] < current_dep_date:
                if get_last_day(get_next_month(self.it_dep_date[-1])) == current_dep_date:
                    break
                self.it_dep_date.append(get_last_day(get_next_month(self.it_dep_date[-1])))
                self.it_accrued.append(self.it_accrued[-1])
                self.it_balance.append(self.it_balance[-1])
                self.it_dep_value.append(self.dep_value)
    
    else:
        current_dep_date = now

    self.it_dep_date.append(current_dep_date)

    if self.it_balance[-1] <= (self.dep_value * gap):
        self.it_accrued.append(self.it_accrued[-1] + (self.it_balance[-1] - 1.00))
        self.it_balance.append(1.00)
        self.it_dep_value.append(self.dep_value)
    else:
        self.it_accrued.append(self.it_accrued[-1] + (self.dep_value * gap))
        self.it_balance.append(self.acquisition_cost - self.it_accrued[-1])
        self.it_dep_value.append(self.dep_value)
    
    zip_list = zip(self.it_dep_date, self.it_dep_value, self.it_accrued, self.it_balance)
    return zip_list


def get_first_day(dt, d_years=0, d_months=0):
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m-1, 12)
    return date(y+a, m+1, 1)


def get_last_day(dt):
    return get_first_day(dt, 0, 1) + timedelta(-1)


def get_gap(p, n):
    if p.year < n.year:
        x = 12 * (n.year - p.year)
        if p.month > n.month:
            y = p.month - n.month
        elif p.month < n.month:
            y = n.month - p.month
        return int(x+y)
    else:
        return -999


def get_next_month(d):
    m = d.month
    if m == 12:
        m = 1
        y = d.year + 1
    else:
        m = d.month + 1
        y = d.year
    return date(y, m, 1)


def get_prev_month(d):
    m = d.month
    if m == 1:
        m = 12
        y = d.year - 1
    else:
        m = d.month - 1
        y = d.year
    return date(y, m, 1)
