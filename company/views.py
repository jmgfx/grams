from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company
from .forms import AddCompanyForm, EditCompanyForm
from branch.models import Branch


def CompanyTable(request):
    context = {
        'companies': Company.objects.filter(display=1)
    }
    return render(request, 'companies.html', context, {'title': 'Companies'})


def ArchivedCompanyTable(request):
    context = {
        'companies': Company.objects.filter(display=0)
    }
    return render(request, 'companiesarchive.html', context, {'title': 'Archived Companies'})


def CompanyView(request, company_id):
    context_view = {
        'company_view': Company.objects.get(id=company_id),
        'branches': Branch.objects.filter(company=company_id),
    }
    return render(request, 'companyview.html', context_view, {'title': 'View Company'})


def CompanyAdd(request):
    if request.method == 'POST':
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)
            new_company.save()
            return redirect('/company/view/' + str(new_company.id))
    else:
        form = AddCompanyForm()
    return render(request, 'addcompany.html', {'form': form}, {'title': 'Add a Company'})


def CompanyEdit(request, company_id):
    if request.method == 'POST':
        form = EditCompanyForm(request.POST, instance=Company.objects.get(id=company_id))
        if form.is_valid():
            form.save()
            return redirect('/company/view/' + str(company_id))
    else:
        form = EditCompanyForm(instance=Company.objects.get(id=company_id))
    return render(request, 'editcompany.html', {'form':form}, {'title': 'Edit a Branch'})


def ArchiveCompany(request, company_id):
    company_to_archive = Company.objects.get(id=company_id)
    company_to_archive.display = 0
    company_to_archive.save()
    return redirect('/company/view/' + str(company_id))


def DeleteCompany(request, company_id):
    company_to_delete = Company.objects.get(id=company_id)
    company_to_delete.delete()
    return redirect('/company/')


def RecoverCompany(request, company_id):
    company_to_recover = Company.objects.get(id=company_id)
    company_to_recover.display = 1
    company_to_recover.save()
    return redirect('/company/view/' + str(company_id))