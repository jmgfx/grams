import datetime
from django import forms
from django.forms import ModelForm, Form, Textarea, TextInput
from .models import Assets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class AddAssetForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddAssetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md mb-0'),
                Column('status', css_class='form-group col-md mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('date_acquired', css_class='form-group col-md mb-0'),
                Column('end_of_warranty', css_class='form-group col-md mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('brand', css_class='form-group col-md mb-0'),
                Column('category', css_class='form-group col-md mb-0'),
                Column('vendor', css_class='form-group col-md mb-0'),
                Column('branch', css_class='form-group col-md mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('model_no', css_class='form-group col-md mb-0'),
                Column('serial_no', css_class='form-group col-md mb-0'),
                css_class='form-row'
            ),
            'specifications',
            Row(
                Column('acquisition_cost', css_class='form-group col-md mb-0'),
                Column('project_life', css_class='form-group col-md mb-0'),
                Column('salvage_value', css_class='form-group col-md mb-0'),
                css_class='form-row'
            ),
            'description',
            Submit('submit', 'New Asset')
        )

    class Meta:
        model = Assets

        fields = ['name', 
                'status', 
                'date_acquired', 
                'end_of_warranty', 
                'brand', 
                'category',
                'vendor',
                'branch',
                'model_no', 
                'serial_no', 
                'specifications',
                'acquisition_cost', 
                'project_life', 
                'salvage_value',
                'description']

        widgets = {
            'date_acquired': forms.TextInput(
                attrs={
                    'type':'date',
                    'placeholder': datetime.date.today(),
                },
            ),
            'end_of_warranty': forms.TextInput(
                attrs={
                    'type':'date',
                    'placeholder': datetime.date.today(),
                },
            ),
            'specifications': Textarea(attrs={
                'rows': 1,
            }),
            'description': Textarea(attrs={
                'rows': 2,
            }),
        }

        labels = {
            'name': 'Asset Name',
            'date_acquired': 'Date Acquired',
            'end_of_warranty': 'End of Warranty',
            'model_no': 'Model Number',
            'serial_no': 'Serial Number',
            'acquisition_cost': 'Acquisition Cost',
            'project_life': 'Projected Life',
            'salvage_value': 'Salvage Value',
        }


class EditAssetForm(ModelForm):
    class Meta:
        model = Assets

        fields = ['name', 
                'end_of_warranty', 
                'specifications',
                'brand', 
                'category',
                'description']

        widgets = {
            'end_of_warranty': forms.TextInput(
                attrs={
                    'type':'date',
                    'placeholder': datetime.date.today(),
                },
            ),
            'specifications': Textarea(attrs={
                'rows': 5,
            }),
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }

        labels = {
            'name': 'Asset Name',
            'end_of_warranty': 'End of Warranty',
            
        }


class RevalueForm(ModelForm):
    class Meta:
        model = Assets
        
        fields = ['acquisition_cost', 
                'project_life', 
                'salvage_value']

        labels = {
            'acquisition_cost': 'Acquisition Cost',
            'project_life': 'Projected Life',
            'salvage_value': 'Salvage Value',
        }
