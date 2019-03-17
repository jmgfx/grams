from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import assetCategory
from .forms import AddAssetCategory, EditAssetCategory
from assets.models import Assets


@login_required
def AssetCategoriesTable(request):
    context = {
        'categories': assetCategory.objects.all()
    }
    return render(request, 'assetcategory.html', context, {'title': 'Asset Categories'})


@login_required
def AssetCategoriesView(request, category_id):
    context_view = {
        'categories_view': assetCategory.objects.get(id=category_id),
        'assets': Assets.objects.filter(category=category_id)
    }
    return render(request, 'assetcategoryview.html', context_view, {'title': 'View Asset Categories'})


@login_required
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


@login_required
def AssetCategoriesEdit(request, category_id):
    if request.method == 'POST':
        form = EditAssetCategory(request.POST, instance=assetCategory.objects.get(id=category_id))
        if form.is_valid():
            form.save()
            return redirect('/assetcategories/view/' + str(category_id))
    else:
        form = EditAssetCategory(instance=assetCategory.objects.get(id=category_id))

    context = {
        'form': form,
        'category': assetCategory.objects.get(id=category_id),
        'title': 'Edit a Category Information',
    }
    return render(request, 'editassetcategory.html', context)


@login_required
def AssetCategoriesDelete(request, category_id):
    category_to_delete = assetCategory.objects.get(id=category_id)
    category_to_delete.delete()
    return redirect('/assetcategories/')