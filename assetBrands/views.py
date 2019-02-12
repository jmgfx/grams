from django.shortcuts import render
from django.http import HttpResponse


def AssetBrandsTable(request):
    return render(request, 'assetbrand.html', {'title': 'Asset Brands'})


def AssetBrandsView(request):
    return render(request, 'assetbrandview.html', {'title': 'View Asset Brand'})


def AssetBrandsAdd(request):
    return render(request, 'addassetbrand.html', {'title': 'Add an Asset Brand'})


def AssetBrandsEdit(request):
    return render(request, 'editassetbrand.html', {'title': 'Edit an Asset Brand'})


def AssetBrandsArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Asset Brands'})
