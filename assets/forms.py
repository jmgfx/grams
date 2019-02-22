from django.forms import ModelForm
from .models import Assets


class AddAssetForm(ModelForm):
    class Meta:
        model = Assets
        fields = ['name', 'quantity', 'status', 
            'date_acquired', 'end_of_warranty', 
            'brand', 'category', 'branch',
            'model_no', 'serial_no',
            'acquisition_cost', 'projected_life', 'salvage_value',
            'description']
       