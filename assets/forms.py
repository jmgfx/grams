import datetime
from django import forms
from django.forms import ModelForm, Form, Textarea, TextInput
from .models import Assets

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class AddAssetForm(ModelForm):
    class Meta:
        model = Assets

        fields = ['name', 
                'quantity', 
                'status', 
                'date_acquired', 
                'end_of_warranty', 
                'brand', 
                'category', 
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
                'rows': 5,
            }),
            'description': Textarea(attrs={
                'rows': 5,
            }),
        }

        labels = {
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
                'quantity',
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
