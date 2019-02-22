from django.shortcuts import render
from django.http import HttpResponse
from .models import Assets
from .forms import AddAssetForm

def AssetTable(request):
    context = {
        'assets': Assets.objects.all()
    }
    return render(request, 'assettable.html', context, {'title': 'Assets'})


def AssetView(request):
    return render(request, 'assetview.html', {'title': 'View Asset'})


def AssetAdd(request):
    if request.method == 'POST':
        form = AddAssetForm(request.POST)
        if form.is_valid():
            new_asset = form.save(commit=False)
            new_asset.save()
    else:
        form = AddAssetForm()
    return render(request, 'addasset.html', {'form': form}, {'title': 'Add an Asset'})


def AssetEdit(request):
    return render(request, 'editasset.html', {'title': 'Edit an Asset'})


def AssetArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Assets'})