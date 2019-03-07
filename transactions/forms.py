from django.forms import ModelForm
from .models import Transactions


class MaintenanceForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['schedule', 'vendor', 'assets_transact']


class TransferForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['branch_origin', 'assets_transact', 'branch_destination']
