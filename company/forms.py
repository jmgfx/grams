from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import Company


class AddCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'owners']

        widgets = {
            'owners': forms.CheckboxSelectMultiple,
        }


class EditCompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'owners']

        widgets = {
            'owners': forms.CheckboxSelectMultiple,
        }