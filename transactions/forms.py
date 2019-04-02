from django import forms
from django.forms import ModelForm, TextInput
from .models import Transactions
from assets.models import Assets


class MaintenanceForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['start_date', 'branch_origin', 'assets_transact']

        widgets = {
            'start_date': forms.TextInput(
                attrs={
                    'type':'date',
                }),
        }

        labels = {
            'start_date': 'Schedule',
            'branch_origin': 'Branch',
            'assets_transact': 'Assets',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets_transact'].queryset = Assets.objects.none()

        if 'branch_origin' in self.data:
            try:
                branch = self.data.get('branch_origin')
                self.fields['assets_transact'].queryset = Assets.objects.filter(branch=branch).filter(display=1)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['assets_transact'].queryset = self.instance.branch_origin.assets_transact_set


class TransferForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['branch_origin', 'assets_transact', 'branch_destination']

        labels = {
            'branch_origin': 'Branch',
            'assets_transact': 'Assets',
            'branch_destination': 'Destination',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets_transact'].queryset = Assets.objects.none()

        if 'branch_origin' in self.data:
            try:
                branch = self.data.get('branch_origin')
                self.fields['assets_transact'].queryset = Assets.objects.filter(branch=branch).filter(display=1)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['assets_transact'].queryset = self.instance.branch_origin.assets_transact_set


class DisposeForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['branch_origin', 'assets_transact']

        labels = {
            'branch_origin': 'Branch',
            'assets_transact': 'Assets',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assets_transact'].queryset = Assets.objects.none()

        if 'branch_origin' in self.data:
            try:
                branch = self.data.get('branch_origin')
                self.fields['assets_transact'].queryset = Assets.objects.filter(branch=branch).filter(display=1)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['assets_transact'].queryset = self.instance.branch_origin.assets_transact_set

    


class RecoverForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['branch_origin', 'archived_assets']

        labels = {
            'branch_origin': 'Branch',
            'archived_assets': 'Assets',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['archived_assets'].queryset = Assets.objects.none()

        if 'branch_origin' in self.data:
            try:
                branch = self.data.get('branch_origin')
                self.fields['archived_assets'].queryset = Assets.objects.filter(branch=branch).filter(display=0)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['archived_assets'].queryset = self.instance.branch_origin.archived_assets_set


class DefectiveForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['branch_origin', 'assets_transact']

        labels = {
            'branch_origin': 'Branch',
            'archived_assets': 'Assets',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['archived_assets'].queryset = Assets.objects.none()

        if 'branch_origin' in self.data:
            try:
                branch = self.data.get('branch_origin')
                self.fields['archived_assets'].queryset = Assets.objects.filter(branch=branch).filter(display=1)
            except(ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['archived_assets'].queryset = self.instance.branch_origin.archived_assets_set
