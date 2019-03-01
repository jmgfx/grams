from django.shortcuts import render
from django.http import HttpResponse
from .models import Vendors
from .forms import AddVendorForm


def VendorsTable(request):
    context = {
        'vendors': Vendors.objects.all()
    }
    return render(request, 'vendors.html', context, {'title': 'Vendors'})


def VendorsView(request, vendor_id):
    context_view = {
        'vendor_view': Vendors.objects.get(id=vendor_id),
    }
    return render(request, 'vendorview.html', context_view, {'title': 'View Vendors'})


def VendorsAdd(request):
    if request.method == 'POST':
        form = AddVendorForm(request.POST)
        if form.is_valid():
            new_vendor = form.save(commit=False)
            new_vendor.save()
    else:
        form = AddVendorForm()
    return render(request, 'addvendor.html', {'form': form}, {'title': 'Add a Vendor'})


def VendorsEdit(request):
    return render(request, 'editvendor.html', {'title': 'Edit a Vendor'})


def VendorsArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Vendors'})