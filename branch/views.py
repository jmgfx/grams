from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Branch
from .forms import AddBranchForm, EditBranchForm
from assets.models import Assets


def BranchTable(request):
    context = {
        'branches': Branch.objects.all()
    }
    return render(request, 'branches.html', context, {'title': 'Branches'})

def BranchView(request, branch_id):
    context_view = {
        'branch_view': Branch.objects.get(id=branch_id),
        'assets': Assets.objects.filter(branch=branch_id),
    }
    return render(request, 'branchview.html', context_view, {'title': 'View Branch'})


def BranchAdd(request):
    if request.method == 'POST':
        form = AddBranchForm(request.POST)
        if form.is_valid():
            new_branch = form.save(commit=False)
            new_branch.save()
            return redirect('/branch/view/' + str(new_branch.id))
    else:
        form = AddBranchForm()
    return render(request, 'addbranch.html', {'form': form}, {'title': 'Add a Branch'})


def BranchEdit(request, branch_id):
    if request.method == 'POST':
        form = EditBranchForm(request.POST, instance=Branch.objects.all().get(id=branch_id))
        if form.is_valid():
            form.save()
            return redirect('/branch/view/' + str(branch_id))
    else:
        form = EditBranchForm(instance=Branch.objects.all().get(id=branch_id))
    return render(request, 'editbranch.html', {'form':form}, {'title': 'Edit a Branch'})


def BranchArchive(request):
    return render(request, 'archive.html', {'title': 'Archived Branches'})