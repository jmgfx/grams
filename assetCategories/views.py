from django.shortcuts import render
from django.http import HttpResponse


def AssetCategoriesTable(request):
    return render(request, 'assetcategory.html', {'title': 'Asset Categories'})

def AssetCategoriesView(request):
    return render(request, 'assetcategoryview.html', {'title': 'View Asset Categories'})


def AssetCategoriesAdd(request):
    return render(request, 'addassetcategory.html', {'title': 'Add an Asset Categories'})


def AssetCategoriesEdit(request):
    return render(request, 'editassetcategory.html', {'title': 'Edit an Asset Categories'})


def AssetCategoriesArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Asset Categories'})