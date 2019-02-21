from django.shortcuts import render
from django.http import HttpResponse
from .models import assetCategory
from .forms import AddAssetCategory


def AssetCategoriesTable(request):
    context = {
        'categories': assetCategory.objects.all()
    }
    return render(request, 'assetcategory.html', context, {'title': 'Asset Categories'})

def AssetCategoriesView(request):
    return render(request, 'assetcategoryview.html', {'title': 'View Asset Categories'})


def AssetCategoriesAdd(request):
    if request.method == 'POST':
        form = AddAssetCategory(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.save()
    else:
        form = AddAssetCategory()
    return render(request, 'addassetcategory.html', {'form': form},{'title': 'Add an Asset Categories'})


def AssetCategoriesEdit(request):
    return render(request, 'editassetcategory.html', {'title': 'Edit an Asset Categories'})


def AssetCategoriesArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Asset Categories'})