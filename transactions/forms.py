from django import forms
from django.forms import ModelForm
from .models import Transactions


class MaintenanceForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['start_date', 'vendor', 'assets_transact']

        widgets = {
            'start_date': forms.SelectDateWidget,
        }


class TransferForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['assets_transact', 'branch_destination']


class DisposeForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['assets_transact']


class RecoverForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['archived_assets']


class DefectiveForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['assets_transact']
