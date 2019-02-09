from django.shortcuts import render
from django.http import HttpResponse


def AssetCategoriesView(request):
    return render(request, '', {'title': 'View Asset Categories'})


def AssetCategoriesAdd(request):
    return render(request, '', {'title': 'Add an Asset Categories'})


def AssetCategoriesEdit(request):
    return render(request, '', {'title': 'Edit an Asset Categories'})


def AssetCategoriesArchive(request):
    return render(request, '', {'title': 'Archived Asset Categories'})