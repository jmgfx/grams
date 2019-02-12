from django.shortcuts import render
from django.http import HttpResponse

def BranchTable(request):
    return render(request, 'branches.html', {'title': 'Branches'})

def BranchView(request):
    return render(request, 'branchview.html', {'title': 'View Branch'})


def BranchAdd(request):
    return render(request, 'addbranch.html', {'title': 'Add a Branch'})


def BranchEdit(request):
    return render(request, 'editbranch.html', {'title': 'Edit a Branch'})


def BranchArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Branches'})