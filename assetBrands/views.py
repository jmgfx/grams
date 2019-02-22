from django.shortcuts import render
from django.http import HttpResponse
from .models import assetBrand
from .forms import AddAssetBrand


def AssetBrandsTable(request):
    context = {
        'brands': assetBrand.objects.all()
    }
    return render(request, 'assetbrand.html', context, {'title': 'Asset Brands'})


def AssetBrandsView(request, brand_id):
    context_view = {
        'brands_view': assetBrand.objects.get(id=brand_id)
    }
    return render(request, 'assetbrandview.html', context_view, {'title': 'View Asset Brand'})


def AssetBrandsAdd(request):
    if request.method == 'POST':
        form = AddAssetBrand(request.POST)
        if form.is_valid():
            new_asset_brand = form.save(commit=False)
            new_asset_brand.save()
    else:
        form = AddAssetBrand()
    return render(request, 'addassetbrand.html', {'form': form}, {'title': 'Add an Asset Brand'})


def AssetBrandsEdit(request):
    return render(request, 'editassetbrand.html', {'title': 'Edit an Asset Brand'})


def AssetBrandsArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Asset Brands'})
