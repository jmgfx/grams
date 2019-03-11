from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Vendors
from .forms import AddVendorForm, EditVendorForm


def VendorsTable(request):
    context = {
        'vendors': Vendors.objects.filter(display=1)
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
            return redirect('/vendors/view/' + str(new_vendor.id))
    else:
        form = AddVendorForm()
    return render(request, 'addvendor.html', {'form': form}, {'title': 'Add a Vendor'})


def VendorsEdit(request, vendor_id):
    if request.method == 'POST':
        form = EditVendorForm(request.POST, instance=Vendors.objects.get(id=vendor_id))
        if form.is_valid():
            form.save()
            return redirect('/vendors/view/' + str(vendor_id))
    else:
        form = EditVendorForm(instance=Vendors.objects.get(id=vendor_id))
    return render(request, 'editvendor.html', {'form':form}, {'title': 'Edit a Vendor'})


def VendorsArchiveTable(request):
    context = {
        'vendors': Vendors.objects.filter(display=0),
        'title': 'Vendors',
    }
    return render(request, 'vendorsarchive.html', context)


def VendorsArchive(request, vendor_id):
    vendor_to_archive = Vendors.objects.get(id=vendor_id)
    vendor_to_archive.display = 0
    vendor_to_archive.save()
    return redirect('/vendors/view/' + str(vendor_id))


def VendorsRecover(request, vendor_id):
    vendor_to_recover = Vendors.objects.get(id=vendor_id)
    vendor_to_recover.display = 1
    vendor_to_recover.save()
    return redirect('/vendors/view/' + str(vendor_id))


def VendorsDelete(request, vendor_id):
    vendor_to_delete = Vendors.objects.get(id=vendor_id)
    vendor_to_delete.delete()
    return redirect('/vendors/')
