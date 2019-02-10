from django.shortcuts import render
from django.http import HttpResponse

def VendorsTable(request):
    return render(request, 'vendors.html', {'title': 'Vendors'})

def VendorsView(request):
    return render(request, '', {'title': 'View Vendors'})


def VendorsAdd(request):
    return render(request, '', {'title': 'Add a Vendor'})


def VendorsEdit(request):
    return render(request, '', {'title': 'Edit a Vendor'})


def VendorsArchive(request):
    return render(request, '', {'title': 'Archived Vendors'})