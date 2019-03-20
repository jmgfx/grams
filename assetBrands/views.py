from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import assetBrand
from .forms import AddAssetBrand, EditAssetBrand
from assets.models import Assets


@login_required
def AssetBrandsTable(request):
    context = {
        'brands': assetBrand.objects.all()
    }
    return render(request, 'assetbrand.html', context, {'title': 'Asset Brands'})


@login_required
def AssetBrandsView(request, brand_id):
    context_view = {
        'brands_view': assetBrand.objects.get(id=brand_id),
        'assets': Assets.objects.filter(brand=brand_id),
    }
    return render(request, 'assetbrandview.html', context_view, {'title': 'View Asset Brand'})


@login_required
def AssetBrandsAdd(request):
    if request.method == 'POST':
        form = AddAssetBrand(request.POST)
        if form.is_valid():
            new_asset_brand = form.save(commit=False)
            new_asset_brand.created_by = request.user
            new_asset_brand.save()
            return redirect('/assetbrands/view/' + str(new_asset_brand.id))
    else:
        form = AddAssetBrand()
    return render(request, 'addassetbrand.html', {'form': form}, {'title': 'Add an Asset Brand'})


@login_required
def AssetBrandsEdit(request, brand_id):
    if request.method == 'POST':
        form = EditAssetBrand(request.POST, instance=assetBrand.objects.get(id=brand_id))
        if form.is_valid():
            new_asset_brand = form.save(commit=False)
            new_asset_brand.save()
            return redirect('/assetbrands/view/' + str(brand_id))
    else:
        form = EditAssetBrand(instance=assetBrand.objects.get(id=brand_id))

    context = {
        'form': form,
        'brand': assetBrand.objects.get(id=brand_id),
        'title': 'Edit a Brand Information',
    }
    return render(request, 'editassetbrand.html', context)


@login_required
def AssetBrandsDelete(request, brand_id):
    brand_to_delete = assetBrand.objects.get(id=brand_id)
    brand_to_delete.delete()
    return redirect('/assetbrands/')
