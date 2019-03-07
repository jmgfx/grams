from django.forms import ModelForm
from .models import Assets


class AddAssetForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'quantity', 'status', 
            'date_acquired', 'end_of_warranty', 
            'brand', 'category', 'branch',
            'model_no', 'serial_no',
            'acquisition_cost', 'project_life', 'salvage_value',
            'description']


class EditAssetForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'quantity', 'status',
            'date_acquired', 'end_of_warranty',
            'brand', 'category', 'branch',
            'description']


class RevalueForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['acquisition_cost', 'project_life', 'salvage_value']
