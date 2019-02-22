from django.shortcuts import render
from django.http import HttpResponse
from .models import Branch
from .forms import AddBranchForm


def BranchTable(request):
    context = {
        'branches': Branch.objects.all()
    }
    return render(request, 'branches.html', context, {'title': 'Branches'})

def BranchView(request, branch_id):
    context_view = {
        'branch_view': Branch.objects.get(id=branch_id)
    }
    return render(request, 'branchview.html', context_view, {'title': 'View Branch'})


def BranchAdd(request):
    if request.method == 'POST':
        form = AddBranchForm(request.POST)
        if form.is_valid():
            new_branch = form.save(commit=False)
            new_branch.save()
    else:
        form = AddBranchForm()
    return render(request, 'addbranch.html', {'form': form}, {'title': 'Add a Branch'})


def BranchEdit(request):
    return render(request, 'editbranch.html', {'title': 'Edit a Branch'})


def BranchArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Branches'})