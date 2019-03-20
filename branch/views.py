from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Branch
from .forms import AddBranchForm, EditBranchForm
from assets.models import Assets


def BranchTable(request):
    context = {
        'branches': Branch.objects.filter(display=1)
    }
    return render(request, 'branches.html', context, {'title': 'Branches'})


def ArchivedBranchTable(request):
    context = {
        'branches': Branch.objects.filter(display=0)
    }
    return render(request, 'branchesarchive.html', context, {'title': 'Archived Branches'})


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
    
    context = {
        'form': form,
        'branch': Branch.objects.get(id=branch_id),
        'title': 'Edit a Branch Information',
    }
    return render(request, 'editbranch.html', context)


def BranchArchive(request, branch_id):
    branch_to_archive = Branch.objects.get(id=branch_id)
    branch_to_archive.display = 0
    branch_to_archive.save()
    return redirect('/branch/view/' + str(branch_id))



def BranchRecover(request, branch_id):
    branch_to_recover = Branch.objects.get(id=branch_id)
    branch_to_recover.display = 1
    branch_to_recover.save()
    return redirect('/branch/view/' + str(branch_id))


def DeleteBranch(request, branch_id):
    branch_to_delete = Branch.objects.get(id=branch_id)
    branch_to_delete.delete()
    return redirect('/branch/')
