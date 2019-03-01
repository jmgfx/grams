from django.forms import ModelForm
from .models import Transactions


class MaintenanceForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ['schedule', 'vendor', 'assets_transact']
