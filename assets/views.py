from django.shortcuts import render
from django.http import HttpResponse


def AssetTable(request):
    return render(request, 'assettable.html', {'title': 'Assets'})

def AssetView(request):
    return render(request, 'assetview.html', {'title': 'View Asset'})


def AssetAdd(request):
    return render(request, 'addasset.html', {'title': 'Add an Asset'})


def AssetEdit(request):
    return render(request, 'editasset.html', {'title': 'Edit an Asset'})


def AssetArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Assets'})