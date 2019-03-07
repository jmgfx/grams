from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import assetCategory
from .forms import AddAssetCategory, EditAssetCategory
from assets.models import Assets


def AssetCategoriesTable(request):
    context = {
        'categories': assetCategory.objects.all()
    }
    return render(request, 'assetcategory.html', context, {'title': 'Asset Categories'})


def AssetCategoriesView(request, category_id):
    context_view = {
        'categories_view': assetCategory.objects.get(id=category_id),
        'assets': Assets.objects.filter(category=category_id)
    }
    return render(request, 'assetcategoryview.html', context_view, {'title': 'View Asset Categories'})


def AssetCategoriesAdd(request):
    if request.method == 'POST':
        form = AddAssetCategory(request.POST)
        if form.is_valid():
            new_category = form.save(commit=False)
            new_category.save()
            return redirect('/assetcategories/view/' + str(new_category.id))
    else:
        form = AddAssetCategory()
    return render(request, 'addassetcategory.html', {'form': form}, {'title': 'Add an Asset Categories'})


def AssetCategoriesEdit(request, category_id):
    if request.method == 'POST':
        form = EditAssetCategory(request.POST, instance=assetCategory.objects.get(id=category_id))
        if form.is_valid():
            form.save()
            return redirect('/assetcategories/view/' + str(category_id))
    else:
        form = EditAssetCategory(instance=assetCategory.objects.get(id=category_id))
    return render(request, 'editassetcategory.html', {'form': form}, {'title': 'Edit an Asset Categories'})


def AssetCategoriesArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Asset Categories'})